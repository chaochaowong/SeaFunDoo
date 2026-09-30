"""Curated database of family-friendly restaurants, bakeries, and post-hike eateries near Seattle trails."""

NEARBY_RESTAURANTS = {
    "discovery park": [
        {
            "name": "Mulleady's Irish Pub & Pantry",
            "cuisine": "Gastropub & Comfort Fare",
            "distance": "0.8 miles from trailhead",
            "vibe": "Cozy, family-welcoming neighborhood spot with hearty burgers and shepherd's pie",
            "kid_friendly": "High chairs, kids menu, great fries",
            "address": "3055 21st Ave W, Seattle, WA 98199",
            "maps_url": "https://maps.google.com/?q=Mulleadys+Seattle+WA"
        },
        {
            "name": "Pink Gorilla Espresso & Bakery",
            "cuisine": "Bakery, Pastries & Espresso",
            "distance": "1.2 miles (Magnolia Village)",
            "vibe": "Local favorite for hot chocolate, warm cinnamon rolls, and fresh cookies after a beach hike",
            "kid_friendly": "Pastries, smoothies, quick grab-and-go",
            "address": "3210 W McGraw St, Seattle, WA 98199",
            "maps_url": "https://maps.google.com/?q=Magnolia+Village+Seattle+WA"
        },
        {
            "name": "Chinn's 32nd Avenue Seafood",
            "cuisine": "Pacific Northwest Seafood & Chowder",
            "distance": "1.4 miles from park",
            "vibe": "Casual clam chowder bowls, fish & chips, and patio seating",
            "kid_friendly": "Crispy fish & chips, kid portions",
            "address": "Magnolia, Seattle, WA",
            "maps_url": "https://maps.google.com/?q=Fish+and+Chips+Magnolia+Seattle+WA"
        }
    ],
    "seward park": [
        {
            "name": "Caffe Vita & Seward Park Clay Studio Cafe",
            "cuisine": "Coffee, Sandwiches & Baked Goods",
            "distance": "0.2 miles (Right at park entrance)",
            "vibe": "Step right off the trail for craft coffee, iced teas, and artisan sandwiches",
            "kid_friendly": "Outdoor grass picnic tables, cookies, Italian sodas",
            "address": "5028 S Ferdinand St, Seattle, WA 98118",
            "maps_url": "https://maps.google.com/?q=Caffe+Vita+Seward+Park+Seattle"
        },
        {
            "name": "Pizzeria Pulcinella",
            "cuisine": "Wood-fired Neapolitan Pizza",
            "distance": "1.0 mile south along Lake Washington Blvd",
            "vibe": "Warm wood oven, authentic thin crust pizzas that kids and parents love",
            "kid_friendly": "Custom kid pizzas, gelato, outdoor patio overlooking the lake",
            "address": "10004 Rainier Ave S, Seattle, WA 98178",
            "maps_url": "https://maps.google.com/?q=Pizzeria+Pulcinella+Seattle"
        },
        {
            "name": "Bent Burgers",
            "cuisine": "Handcrafted Gourmet Burgers & Shakes",
            "distance": "1.3 miles (Columbia City)",
            "vibe": "Vibrant burger shack with real milkshakes and crispy onion rings",
            "kid_friendly": "Kid-sized smash burgers, thick milkshakes",
            "address": "Columbia City, Seattle, WA",
            "maps_url": "https://maps.google.com/?q=Columbia+City+Burgers+Seattle"
        }
    ],
    "washington park arboretum": [
        {
            "name": "Cafe Flora",
            "cuisine": "Farm-to-Table Vegetarian / PNW Cafe",
            "distance": "0.7 miles (Madison Valley)",
            "vibe": "Iconic Seattle greenhouse atrium dining, legendary weekend brunch and kid bento boxes",
            "kid_friendly": "Celebrated kids menu, toy baskets, fruit skewers, quesadillas",
            "address": "2901 E Madison St, Seattle, WA 98112",
            "maps_url": "https://maps.google.com/?q=Cafe+Flora+Seattle"
        },
        {
            "name": "The Harvest Vine",
            "cuisine": "Spanish Tapas & Pastries",
            "distance": "0.6 miles",
            "vibe": "Intimate European feel with freshly baked sourdough and hot churros",
            "kid_friendly": "Churros con chocolate, small savory bites",
            "address": "2701 E Madison St, Seattle, WA 98112",
            "maps_url": "https://maps.google.com/?q=The+Harvest+Vine+Seattle"
        }
    ],
    "twin falls": [
        {
            "name": "Twede's Cafe (The Double R Diner)",
            "cuisine": "Classic American Diner & Twin Peaks Cherry Pie",
            "distance": "3.5 miles (Historic Downtown North Bend)",
            "vibe": "Famous from Twin Peaks! Classic booth seating, hearty burgers, and huge slices of cherry pie",
            "kid_friendly": "Kids pancakes, milkshakes, coloring placemats",
            "address": "137 W North Bend Way, North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=Twedes+Cafe+North+Bend+WA"
        },
        {
            "name": "Rio Bravo Tacos",
            "cuisine": "Fresh Mexican & Burritos",
            "distance": "3.2 miles",
            "vibe": "Casual, fast, flavorful tacos, quesadillas, and house-made salsas",
            "kid_friendly": "Cheese quesadillas, mild carnitas, outdoor tables",
            "address": "247 E North Bend Way, North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=Rio+Bravo+North+Bend+WA"
        }
    ],
    "rattlesnake ledge": [
        {
            "name": "South Fork Bakery & Deli",
            "cuisine": "Artisan Sandwiches, Soups & Bakery",
            "distance": "4.5 miles (North Bend)",
            "vibe": "Post-hike carb heaven with fresh sourdough sandwiches, hot clam chowder, and chocolate chip cookies",
            "kid_friendly": "Grilled cheese, cookies, fresh lemonades",
            "address": "North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=North+Bend+Bakery+WA"
        },
        {
            "name": "North Bend Bar & Grill",
            "cuisine": "Pacific Northwest Pub & Grill",
            "distance": "4.8 miles",
            "vibe": "Rustic lodge atmosphere with fireside booths, local draft cider, and salmon sliders",
            "kid_friendly": "Spacious booths, full kids menu, mac & cheese",
            "address": "145 E North Bend Way, North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=North+Bend+Bar+and+Grill+WA"
        }
    ],
    "little si": [
        {
            "name": "Twede's Cafe",
            "cuisine": "Historic Diner & Legendary Cherry Pie",
            "distance": "2.2 miles (Downtown North Bend)",
            "vibe": "Famous diner booths serving hearty burger platters and famous pie with soft serve",
            "kid_friendly": "High chairs, shakes, kids breakfast menu",
            "address": "137 W North Bend Way, North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=Twedes+Cafe+North+Bend+WA"
        },
        {
            "name": "Il Paesano Ristorante",
            "cuisine": "Italian & Pasta",
            "distance": "2.0 miles",
            "vibe": "Family-run, comforting bowls of fettuccine, warm garlic bread, and pizza",
            "kid_friendly": "Kids pasta bowls, friendly staff",
            "address": "North Bend, WA 98045",
            "maps_url": "https://maps.google.com/?q=Italian+Restaurant+North+Bend+WA"
        }
    ],
    "bridle trails": [
        {
            "name": "Burgermaster",
            "cuisine": "Classic Drive-In Burgers & Malts",
            "distance": "1.5 miles (Kirkland/Bellevue border)",
            "vibe": "Historic PNW carhop drive-in beloved by local families since 1952",
            "kid_friendly": "Kids love eating right in the car or on patio, crinkle fries, malt shakes",
            "address": "10606 NE 8th St, Bellevue, WA 98004",
            "maps_url": "https://maps.google.com/?q=Burgermaster+Bellevue+WA"
        },
        {
            "name": "Zaucer Pizza",
            "cuisine": "Sci-Fi Themed Artisan Pizza",
            "distance": "1.8 miles",
            "vibe": "Playful atmosphere with comic books, arcade games, and creative pizzas",
            "kid_friendly": "Games, kid-sized pies, fun alien decor",
            "address": "Kirkland, WA",
            "maps_url": "https://maps.google.com/?q=Pizza+Kirkland+WA"
        }
    ],
    "coal creek": [
        {
            "name": "The Golf Club at Newcastle - The Calcutta Grill",
            "cuisine": "American Grill with Panoramic Seattle Skyline Views",
            "distance": "2.0 miles up the ridge",
            "vibe": "Breathtaking panoramic view of Lake Washington and the Seattle skyline",
            "kid_friendly": "Expansive outdoor patio lawns, kids burger and pasta menu",
            "address": "15500 Six Newcastle Golf Club Rd, Newcastle, WA 98059",
            "maps_url": "https://maps.google.com/?q=The+Calcutta+Grill+Newcastle+WA"
        },
        {
            "name": "Frosty Barrel Ice Cream & Cafe",
            "cuisine": "Artisan Small-Batch Ice Cream",
            "distance": "1.5 miles (Newcastle Village)",
            "vibe": "The ultimate sweet reward after hiking Coal Creek trails",
            "kid_friendly": "Waffle cones, flights of scoops, dairy-free fruit sorbets",
            "address": "Newcastle, WA",
            "maps_url": "https://maps.google.com/?q=Ice+Cream+Newcastle+WA"
        }
    ]
}

def get_nearby_restaurants(trail_or_city: str) -> list:
    """Find curated family restaurants near a given trail or area."""
    key = trail_or_city.lower().strip()
    for trail_key, spots in NEARBY_RESTAURANTS.items():
        if trail_key in key or key in trail_key:
            return spots
    # Default fallback to Seattle favorites
    return NEARBY_RESTAURANTS.get("discovery park", [])
