# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo
from typing import Optional, List, Dict, Any

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from .trails_data import TRAILS_DB
from .restaurants_data import get_nearby_restaurants, NEARBY_RESTAURANTS
from .firestore_db import (
    get_all_trails_from_firestore,
    get_trail_by_name_from_firestore,
    save_trail_to_firestore,
    PROJECT_ID,
    COLLECTION_NAME,
)

MODEL = "gemini-3.6-flash"


def search_seattle_trails(
    difficulty: Optional[str] = None,
    stroller_friendly: Optional[bool] = None,
    dog_friendly: Optional[bool] = None,
    max_distance_miles: Optional[float] = None,
    keyword: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Search and filter family-friendly hiking trails in the greater Seattle and Puget Sound area.

    Args:
        difficulty: Optional difficulty filter ('Easy', 'Moderate', or 'Moderate to Strenuous').
        stroller_friendly: If True, only returns trails suitable for strollers/wagons.
        dog_friendly: If True, only returns trails allowing dogs on leash.
        max_distance_miles: Maximum round-trip trail length in miles.
        keyword: Search term to match against trail name, location, or highlights (e.g. 'waterfall', 'beach', 'lake', 'boardwalk').

    Returns:
        A list of matching trail dictionaries including map links and coordinates.
    """
    # Fetch trails from Firestore backend or local cache
    try:
        source_trails = get_all_trails_from_firestore()
        if not source_trails:
            source_trails = TRAILS_DB
    except Exception:
        source_trails = TRAILS_DB

    results = []
    kw = keyword.lower() if keyword else None
    diff = difficulty.lower() if difficulty else None

    for trail in source_trails:
        if stroller_friendly is not None and trail.get("stroller_friendly") != stroller_friendly:
            continue
        if dog_friendly is not None and trail.get("dog_friendly") != dog_friendly:
            continue
        if max_distance_miles is not None and trail.get("distance_miles", 0) > max_distance_miles:
            continue
        if diff and diff not in trail.get("difficulty", "").lower():
            continue
        if kw:
            text = f"{trail.get('name', '')} {trail.get('location', '')} {trail.get('description', '')} {' '.join(trail.get('highlights', []))}".lower()
            if kw not in text:
                continue
        results.append(trail)

    return results


def get_trail_details(trail_name: str) -> Dict[str, Any]:
    """Retrieve full details, pass requirements, coordinates, and family highlights for a specific trail.

    Args:
        trail_name: The name or partial name of the trail (e.g., 'Discovery Park', 'Twin Falls', 'Rattlesnake').

    Returns:
        Full dictionary of trail information and Google Maps links.
    """
    try:
        fs_trail = get_trail_by_name_from_firestore(trail_name)
        if fs_trail:
            return fs_trail
    except Exception:
        pass

    tn = trail_name.lower().strip()
    for trail in TRAILS_DB:
        if tn in trail["name"].lower() or trail["name"].lower() in tn:
            return trail

    return {
        "error": f"Trail '{trail_name}' not found. Try 'Discovery Park', 'Seward Park', 'Twin Falls', or 'Rattlesnake Ledge'."
    }


def add_custom_trail_record(
    name: str,
    location: str,
    distance_miles: float,
    elevation_gain_ft: int,
    difficulty: str,
    stroller_friendly: bool,
    dog_friendly: bool,
    pass_required: str,
    highlights: List[str],
    description: str,
    best_for: str = "Families"
) -> Dict[str, Any]:
    """Save a new family trail or custom community hiking spot to the Firestore backend.

    Args:
        name: Name of the trail (e.g., 'Cougar Mountain Red Town Trail').
        location: City/neighborhood (e.g., 'Bellevue / Newcastle').
        distance_miles: Total round trip distance in miles.
        elevation_gain_ft: Total elevation gain in feet.
        difficulty: 'Easy', 'Moderate', or 'Strenuous'.
        stroller_friendly: True if safe for strollers/wagons.
        dog_friendly: True if dogs are allowed on-leash.
        pass_required: Required parking pass (e.g. 'None (Free)', 'Discover Pass').
        highlights: List of key family highlights (views, playgrounds, etc.).
        description: Informative overview of the trail.
        best_for: Target audience (e.g., 'Toddlers', 'Kids 6+').

    Returns:
        Confirmation dictionary with the saved document ID in Firestore.
    """
    doc_id = name.lower().replace(" ", "-").replace("'", "")
    new_doc = {
        "id": doc_id,
        "name": name,
        "location": location,
        "distance_miles": distance_miles,
        "elevation_gain_ft": elevation_gain_ft,
        "difficulty": difficulty,
        "stroller_friendly": stroller_friendly,
        "dog_friendly": dog_friendly,
        "pass_required": pass_required,
        "highlights": highlights,
        "description": description,
        "best_for": best_for,
        "map_url": f"https://maps.google.com/?q={name.replace(' ', '+')}+{location.replace(' ', '+')}",
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    saved_id = save_trail_to_firestore(new_doc)
    return {
        "status": "success",
        "message": f"Successfully recorded '{name}' to Firestore collection '{COLLECTION_NAME}' (Project: {PROJECT_ID})",
        "document_id": saved_id,
        "trail": new_doc
    }


def list_firestore_trails() -> List[Dict[str, Any]]:
    """List all trails stored directly in the Firestore 'seattle_trails' collection.

    Returns:
        A list of trail documents currently saved in the Firestore database.
    """
    return get_all_trails_from_firestore()


def get_trail_map(trail_name: str) -> Dict[str, Any]:
    """Get the GPS coordinates, interactive map URL, and Google Maps direction link for a trail.

    Args:
        trail_name: Name of the trail.

    Returns:
        Coordinates, Google Maps URL, and embed URL.
    """
    details = get_trail_details(trail_name)
    if "error" in details:
        return details

    coords = details.get("coordinates")
    embed_url = details.get("embed_map_url")
    if not embed_url and coords:
        embed_url = f"https://maps.google.com/maps?q={coords['lat']},{coords['lng']}&z=14&output=embed"

    return {
        "trail_name": details["name"],
        "coordinates": coords,
        "google_maps_url": details.get("map_url"),
        "embed_map_url": embed_url,
        "parking_info": f"Pass required: {details.get('pass_required')}"
    }


def plan_family_trail_trip(
    trail_name: str,
    family_members: str,
    start_time: str = "9:00 AM",
    pace: str = "leisurely"
) -> Dict[str, Any]:
    """Generate a tailored family trip itinerary, map directions, and packing recommendations for a Seattle trail hike.

    Args:
        trail_name: The destination trail name.
        family_members: Description of who is going, including children's ages (e.g. 'parents with 4yo and 7yo', 'toddler in stroller and dog').
        start_time: Desired start time (e.g., '9:30 AM').
        pace: Pace preference ('leisurely' with frequent stops, or 'steady').

    Returns:
        A planned timeline, map directions link, packing checklist, parking advice, and safety notes.
    """
    details = get_trail_details(trail_name)
    if "error" in details:
        return details

    stroller_note = "Bring a rugged or all-terrain stroller/wagon." if details.get("stroller_friendly") else "Trail is not stroller friendly; use a baby/toddler carrier backpack instead."
    pass_note = f"Pass required: {details.get('pass_required')}."

    return {
        "trail": details["name"],
        "location": details["location"],
        "google_maps_url": details.get("map_url"),
        "embed_map_url": details.get("embed_map_url"),
        "family_profile": family_members,
        "suggested_timeline": [
            {"time": start_time, "activity": f"Arrive at trailhead / parking. {pass_note} Display pass if needed. Check restrooms."},
            {"time": "+15 mins", "activity": "Lace up shoes, apply sunscreen/bug spray, pack water bottles and first batch of snacks."},
            {"time": "+45 mins", "activity": f"Halfway / scenic rest stop: {details['highlights'][0] if details.get('highlights') else 'Scenic vista'}. Great spot for kids' snack break and photos."},
            {"time": "+1h 30m", "activity": f"Complete loop or main trail vista. Enjoy {details.get('best_for', 'nature')}."},
            {"time": "+2h 00m", "activity": "Picnic lunch or head to nearby local family cafe / ice cream."}
        ],
        "kid_friendly_tips": [
            stroller_note,
            "PNW weather tip: Layer with breathable rain jackets and sturdy footwear with good traction.",
            "Keep emergency high-protein snacks (applesauce pouches, trail mix, fruit snacks) readily accessible.",
            "Leave No Trace: Pack a small trash bag for diaper/snack wrapper disposal."
        ],
        "pass_and_parking": details.get("pass_required", "None")
    }


def recommend_nearby_restaurants(trail_or_city: str) -> Dict[str, Any]:
    """Recommend family-friendly restaurants, bakeries, cafes, and ice cream shops near a trail or neighborhood.

    Args:
        trail_or_city: The trail name or neighborhood (e.g., 'Discovery Park', 'Twin Falls', 'Seward Park', 'Rattlesnake Ledge', 'North Bend', 'Magnolia').

    Returns:
        A list of recommended eateries with cuisine, vibe, kid-friendly perks, and Google Maps directions links.
    """
    eateries = get_nearby_restaurants(trail_or_city)
    return {
        "destination": trail_or_city,
        "recommendations": eateries,
        "tip": "Call ahead or check hours for weekend brunch/post-hike lunch rushes!"
    }


def get_weather(query: str) -> str:
    """Get current weather conditions and outdoor recreation forecast.

    Args:
        query: The location or city to get weather for (e.g., 'Seattle', 'North Bend', 'Bellevue').

    Returns:
        Formatted weather report for outdoor activities.
    """
    q = query.lower()
    if "seattle" in q or "magnolia" in q or "bellevue" in q or "kirkland" in q or "north bend" in q:
        return (
            "Seattle / Puget Sound regional weather: 64°F, partly cloudy with mild ocean breeze, "
            "0% chance of rain today. Excellent conditions for family trail hiking and outdoor picnics!"
        )
    return "It's 70°F and sunny with mild winds. Great day for outdoor exploration."


def get_current_time(query: str = "Seattle") -> str:
    """Gets the current local Pacific time.

    Args:
        query: City or timezone query (defaults to Seattle / Pacific Time).

    Returns:
        Formatted local time string.
    """
    tz = ZoneInfo("America/Los_Angeles")
    now = datetime.datetime.now(tz)
    return f"The current time in Seattle/Pacific is {now.strftime('%A, %B %d, %Y at %I:%M %p %Z')}."


root_agent = Agent(
    name="seafundoo",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are SeaFunDoo, a fun, warm, knowledgeable local Pacific Northwest hiking, outdoor family adventure guide and trail concierge.

Your mission is to help families with kids of all ages (from infants and toddlers to teenagers) discover and enjoy local trails in Seattle and the surrounding Puget Sound area.

Key capabilities:
1. Search and query trails backed by Google Cloud Firestore (`seattle_trails` collection).
2. Save new community or user-recommended family trails into Firestore (`add_custom_trail_record`).
3. Look up detailed trail specifications, parking pass requirements, and interactive maps.
4. Recommend family-friendly restaurants, diners, cafes, and ice cream shops near trailheads (`recommend_nearby_restaurants`).
5. Provide direct Google Maps navigation links and embeddable map links whenever discussing or planning a trail trip so families can easily navigate there.
6. Build practical, realistic family trip itineraries including packing checklists, rest stops, meal breaks, and timing.
7. Provide local Pacific Northwest weather and recreation advice.

Always include the trail or restaurant location and a clickable Google Maps link in your recommendations so users can view the map immediately.
""",
    tools=[
        search_seattle_trails,
        get_trail_details,
        list_firestore_trails,
        add_custom_trail_record,
        get_trail_map,
        plan_family_trail_trip,
        recommend_nearby_restaurants,
        get_weather,
        get_current_time
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
