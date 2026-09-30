"""Firestore client and helpers for the Seattle Family Trail Concierge.

Important: Hardcodes project ID as a string to prevent Agent Platform
project-number resolution bugs in Google Cloud.
"""

from typing import List, Dict, Any, Optional
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-04-fe0edf1960f2"
COLLECTION_NAME = "seattle_trails"

def get_firestore_client() -> firestore.Client:
    """Return an authenticated Firestore client with hardcoded project ID."""
    return firestore.Client(project=PROJECT_ID)

def get_all_trails_from_firestore() -> List[Dict[str, Any]]:
    """Retrieve all trails from the Firestore 'seattle_trails' collection."""
    db = get_firestore_client()
    docs = db.collection(COLLECTION_NAME).stream()
    trails = []
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        trails.append(data)
    return trails

def get_trail_by_name_from_firestore(trail_name: str) -> Optional[Dict[str, Any]]:
    """Query a trail by name from Firestore."""
    db = get_firestore_client()
    tn = trail_name.lower().strip()
    
    # Try exact or case-insensitive search across documents
    docs = db.collection(COLLECTION_NAME).stream()
    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        name = data.get("name", "").lower()
        if tn in name or name in tn:
            return data
    return None

def save_trail_to_firestore(trail_data: Dict[str, Any]) -> str:
    """Save or update a trail document in the Firestore collection."""
    db = get_firestore_client()
    doc_id = trail_data.get("id") or trail_data.get("name", "").lower().replace(" ", "-")
    doc_ref = db.collection(COLLECTION_NAME).document(doc_id)
    doc_ref.set(trail_data, merge=True)
    return doc_id
