"""Curated database of Seattle-area hiking trails with family and kid-friendly attributes."""

TRAILS_DB = [
    {
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
        "embed_map_url": "https://maps.google.com/maps?q=47.6575,-122.4060&z=14&output=embed",
        "highlights": [
            "Puget Sound & Olympic mountain views",
            "Sandy beach & historic lighthouse",
            "Large children's playground",
            "Restrooms at Visitor Center & beach"
        ],
        "description": "Seattle's largest public park offering tidal beaches, sea cliffs, forest groves, and open meadows. The paved loop is accessible for rugged strollers.",
        "best_for": "Toddlers, all ages, beach picnics, views"
    },
    {
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
        "embed_map_url": "https://maps.google.com/maps?q=47.5495,-122.2570&z=14&output=embed",
        "highlights": [
            "Flat paved path on Lake Washington shoreline",
            "Old-growth forest interior trails",
            "Mount Rainier views on clear days",
            "Playground, swimming beach, Audubon center"
        ],
        "description": "Completely paved and flat shoreline loop jutting into Lake Washington. Exceptionally stroller, wagon, and scooter-friendly for families with younger kids.",
        "best_for": "Strollers, scooters, toddlers, picnics"
    },
    {
        "name": "Washington Park Arboretum & Foster Island",
        "location": "Montlake / Madison Park, Seattle",
        "distance_miles": 2.0,
        "elevation_gain_ft": 50,
        "difficulty": "Easy",
        "stroller_friendly": True,
        "dog_friendly": True,
        "pass_required": "None (Free)",
        "coordinates": {"lat": 47.6360, "lng": -122.2965},
        "map_url": "https://maps.google.com/?q=Washington+Park+Arboretum+Graham+Visitors+Center",
        "embed_map_url": "https://maps.google.com/maps?q=47.6360,-122.2965&z=14&output=embed",
        "highlights": [
            "Wooden boardwalks over wetland waters",
            "Water lilies, turtles, bird watching",
            "Arboretum botanical collections",
            "Lake Washington waterfront"
        ],
        "description": "Wander through world-class tree collections and take the boardwalk over wetlands to Foster Island. Kids love seeing ducks, kayakers, and floating pathways.",
        "best_for": "Young kids, nature discovery, flat strolls"
    },
    {
        "name": "Bridle Trails State Park",
        "location": "Kirkland / Bellevue (Eastside)",
        "distance_miles": 3.2,
        "elevation_gain_ft": 100,
        "difficulty": "Easy",
        "stroller_friendly": False,
        "dog_friendly": True,
        "pass_required": "Washington Discover Pass",
        "coordinates": {"lat": 47.6534, "lng": -122.1812},
        "map_url": "https://maps.google.com/?q=Bridle+Trails+State+Park+Kirkland+WA",
        "embed_map_url": "https://maps.google.com/maps?q=47.6534,-122.1812&z=14&output=embed",
        "highlights": [
            "Horse sightings on equestrian trails",
            "Dense evergreen canopy (great on rainy or hot days)",
            "Well-marked interconnected loops"
        ],
        "description": "A tranquil 482-acre forested oasis just minutes from downtown Bellevue. Gentle rolling dirt paths under towering Douglas firs where children often spot real horses.",
        "best_for": "Forest walks, animal-loving kids, shaded hiking"
    },
    {
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
        "embed_map_url": "https://maps.google.com/maps?q=47.4533,-121.7032&z=14&output=embed",
        "highlights": [
            "Dramatic multi-tiered cascading waterfalls",
            "Suspension bridge over the Snoqualmie river",
            "Old-growth trees & mossy boulders"
        ],
        "description": "One of the premier family waterfall hikes near Seattle. Follows the South Fork Snoqualmie River through lush rain forest to a wooden viewing bridge.",
        "best_for": "Kids 6+, waterfall enthusiasts, adventure walks"
    },
    {
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
        "embed_map_url": "https://maps.google.com/maps?q=47.4347,-121.7684&z=14&output=embed",
        "highlights": [
            "Panoramic cliffside view of Rattlesnake Lake and Snoqualmie Pass",
            "Rattlesnake Lake park with flat shoreline paths below"
        ],
        "description": "A classic Pacific Northwest hike with switchbacks through tall forest ending at an exposed rocky ledge. The lake at the base is flat and toddler-friendly, while the ledge hike is great for older energetic kids.",
        "best_for": "Kids 8+, teens, big summit views"
    },
    {
        "name": "Coal Creek Trail",
        "location": "Bellevue / Newcastle (Cougar Mountain)",
        "distance_miles": 3.0,
        "elevation_gain_ft": 250,
        "difficulty": "Easy to Moderate",
        "stroller_friendly": False,
        "dog_friendly": True,
        "pass_required": "None (Free King County Park)",
        "coordinates": {"lat": 47.5539, "lng": -122.1587},
        "map_url": "https://maps.google.com/?q=Red+Town+Trailhead+Coal+Creek+Park",
        "embed_map_url": "https://maps.google.com/maps?q=47.5539,-122.1587&z=14&output=embed",
        "highlights": [
            "Historic 19th-century coal mine carts & railroad grades",
            "Wooden bridges, small waterfalls, creek exploration"
        ],
        "description": "A rich walk through mining history along bubbling Coal Creek. Kids love spotting remnants of old railways, mine shafts, and wooden bridge crossings.",
        "best_for": "Elementary-age kids, history lovers, shady creek walks"
    }
]
