"""FastAPI web server for SeaFunDoo - Seattle Family Trail Concierge.
Runs locally, connects to the local ADK agent instance in simple-agent,
and provides trail listing, map views, facts, and chat.
"""

import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any

# Configure Vertex AI environment for the local runner
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "qwiklabs-gcp-04-fe0edf1960f2"
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

# Add simple-agent to path so we can invoke agent logic directly and instantly
AGENT_DIR = Path("/config/Desktop/BuildWithGemini/simple-agent")
sys.path.insert(0, str(AGENT_DIR))

from app.trails_data import TRAILS_DB
from app.restaurants_data import get_nearby_restaurants
from app.agent import (
    search_seattle_trails,
    get_trail_details,
    get_trail_map,
    plan_family_trail_trip,
    recommend_nearby_restaurants,
    get_weather,
    root_agent,
)
from google.adk.runners import InMemoryRunner
from google.genai import types

app = FastAPI(title="SeaFunDoo - Seattle Family Trail Concierge")

# Reusable runner and session
runner = InMemoryRunner(agent=root_agent)
session_holder = {"id": None}

async def get_or_create_session_id():
    if not session_holder["id"]:
        session = await runner.session_service.create_session(app_name=runner.app_name, user_id="web_user")
        session_holder["id"] = session.id
    return session_holder["id"]

class ChatRequest(BaseModel):
    message: str

@app.get("/api/trails")
def list_trails():
    """Return all available trails with metadata and coordinates."""
    # Enhance each trail with nearby restaurants
    enriched = []
    for t in TRAILS_DB:
        t_copy = dict(t)
        t_copy["restaurants"] = get_nearby_restaurants(t["name"])
        enriched.append(t_copy)
    return enriched

@app.get("/api/trails/{trail_name}")
def trail_details(trail_name: str):
    """Return details, coordinates, highlights, and tips for a trail."""
    details = get_trail_details(trail_name)
    if "error" in details:
        raise HTTPException(status_code=404, detail=details["error"])
    details["restaurants"] = get_nearby_restaurants(trail_name)
    return details

@app.get("/api/restaurants/{trail_name}")
def nearby_restaurants_endpoint(trail_name: str):
    """Return family-friendly restaurant recommendations near a specific trail."""
    return {"trail": trail_name, "restaurants": get_nearby_restaurants(trail_name)}

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """Process user queries through the trail concierge agent."""
    user_msg = req.message.strip()
    if not user_msg:
        return {"reply": "Please ask a question about Seattle trails!"}

    collected_texts = []
    try:
        session_id = await get_or_create_session_id()
        user_content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_msg)]
        )
        async for event in runner.run_async(
            new_message=user_content,
            session_id=session_id,
            user_id="web_user"
        ):
            if event.content and event.content.parts:
                for p in event.content.parts:
                    if p.text:
                        collected_texts.append(p.text)

        reply_text = "".join(collected_texts).strip()
        if not reply_text:
            reply_text = "I've checked the local trail database. How can I help you plan your hike today?"
    except Exception as e:
        # Fallback to local keyword search if any error occurs
        q_lower = user_msg.lower()
        matched = None
        for t in TRAILS_DB:
            if t["name"].lower() in q_lower or any(word in q_lower for word in t["name"].lower().split()):
                matched = t
                break
        if matched:
            reply_text = (
                f"**{matched['name']}** ({matched['location']})\n\n"
                f"- **Distance:** {matched['distance_miles']} miles\n"
                f"- **Elevation Gain:** {matched['elevation_gain_ft']} ft\n"
                f"- **Difficulty:** {matched['difficulty']}\n"
                f"- **Stroller Friendly:** {'Yes' if matched['stroller_friendly'] else 'No'}\n"
                f"- **Pass:** {matched['pass_required']}\n\n"
                f"{matched['description']}"
            )
        else:
            reply_text = f"I'm here to help you plan your Seattle trail trip! Try selecting a trail on the left panel or asking about stroller-friendly walks, waterfall hikes, or Discovery Park."

    return {"reply": reply_text}

# Mount static files
STATIC_DIR = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
