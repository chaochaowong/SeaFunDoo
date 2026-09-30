"""Seed script for populating Seattle local trails in Google Cloud Firestore.

Hardcodes the GCP project ID string to prevent Agent Platform project-number resolution issues.
"""

from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-04-fe0edf1960f2"
COLLECTION_NAME = "seattle_trails"

SEEDED_TRAILS = [
    {
        "id": "discovery-park-loop",
        "name": "Discovery Park Loop Trail",
        "location": "Magnolia, Seattle",
        "distance_miles": 2.8,
        "elevation_gain_ft": 140,
        "difficulty": "Easy",
        "stroller_friendly": True,
        "dog_friendly": True,
        "pass_required": "None (Free City Park)",
        "coordinates": {"lat": 47.6575, "lng": -122.4060},
        "map_url": "https://maps.google.com/?q=Discovery+Park+Visitor+Center+Seattle+WA",
        "highlights": [
            "Puget Sound & Olympic mountain views",
            "Sandy beach & historic lighthouse",
            "Large children's playground",
            "Restrooms at Visitor Center & beach"
        ],
        "description": "Seattle's largest public park offering tidal beaches, sea cliffs, forest groves, and open meadows.",
        "best_for": "Toddlers, all ages, beach picnics, views",
        "family_notes": "Main loop path is wide and accessible with an all-terrain stroller/wagon."
    },
    {
        "id": "seward-park-loop",
        "name": "Seward Park Perimeter Loop",
        "location": "Lake Washington, South Seattle",
        "distance_miles": 2.4,
        "elevation_gain_ft": 20,
        "difficulty": "Easy",
        "stroller_friendly": True,
        "dog_friendly": True,
        "pass_required": "None (Free City Park)",
        "coordinates": {"lat": 47.5495, "lng": -122.2570},
        "map_url": "https://maps.google.com/?q=Seward+Park+Loop+Trail+Seattle+WA",
        "highlights": [
            "Flat paved path on Lake Washington shoreline",
            "Old-growth forest interior trails",
            "Mount Rainier views on clear days",
            "Playground, swimming beach, Audubon center"
        ],
        "description": "Completely paved and flat shoreline loop jutting into Lake Washington.",
        "best_for": "Strollers, scooters, toddlers, picnics",
        "family_notes": "100% paved; perfect for scooters, balance bikes, and standard strollers."
    },
    {
        "id": "twin-falls",
        "name": "Twin Falls Trail",
        "location": "North Bend (I-90 Corridor)",
        "distance_miles": 2.6,
        "elevation_gain_ft": 500,
        "difficulty": "Moderate",
        "stroller_friendly": False,
        "dog_friendly": True,
        "pass_required": "Washington Discover Pass",
        "coordinates": {"lat": 47.4533, "lng": -121.7032},
        "map_url": "https://maps.google.com/?q=Twin+Falls+Trailhead+North+Bend+WA",
        "highlights": [
            "Dramatic multi-tiered cascading waterfalls",
            "Suspension bridge over the Snoqualmie river",
            "Old-growth trees & mossy boulders"
        ],
        "description": "Follows the South Fork Snoqualmie River through lush rain forest to a wooden viewing bridge.",
        "best_for": "Kids 6+, waterfall enthusiasts, adventure walks",
        "family_notes": "Not stroller friendly. Kids love the roaring waterfall and suspension bridge."
    },
    {
        "id": "rattlesnake-ledge",
        "name": "Rattlesnake Ledge",
        "location": "North Bend / Snoqualmie Valley",
        "distance_miles": 4.0,
        "elevation_gain_ft": 1160,
        "difficulty": "Moderate to Strenuous",
        "stroller_friendly": False,
        "dog_friendly": True,
        "pass_required": "None (City of Seattle Watershed)",
        "coordinates": {"lat": 47.4347, "lng": -121.7684},
        "map_url": "https://maps.google.com/?q=Rattlesnake+Ledge+Trailhead+North+Bend+WA",
        "highlights": [
            "Panoramic cliffside view of Rattlesnake Lake and Snoqualmie Pass",
            "Rattlesnake Lake park with flat shoreline paths below"
        ],
        "description": "A classic Pacific Northwest hike with switchbacks through tall forest ending at an exposed rocky ledge.",
        "best_for": "Kids 8+, teens, big summit views",
        "family_notes": "Lake shoreline below is stroller friendly; upper climb has steep drop-offs at summit."
    }
]

def seed_firestore():
    print(f"Connecting to Firestore with hardcoded project ID: '{PROJECT_ID}'...")
    db = firestore.Client(project=PROJECT_ID)
    collection = db.collection(COLLECTION_NAME)

    for item in SEEDED_TRAILS:
        doc_id = item["id"]
        doc_ref = collection.document(doc_id)
        doc_ref.set(item)
        print(f"  ✓ Seeded document '{doc_id}': {item['name']}")

    print(f"Successfully seeded {len(SEEDED_TRAILS)} trails into collection '{COLLECTION_NAME}'!")

if __name__ == "__main__":
    seed_firestore()
