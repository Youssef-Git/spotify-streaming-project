import uuid
import random
import json
#from datetime import datetime
from datetime import datetime, timezone

# Reference data
USERS = [{"user_id": str(uuid.uuid4()), "country": country, "platform": platform}
    for country, platform in [
        ("France", "mobile"), ("USA", "desktop"), ("UK", "mobile"),
        ("Germany", "web"), ("Spain", "desktop"), ("Italy", "mobile"),
        ("Belgium", "web"), ("Canada", "desktop"), ("Brazil", "mobile"),
        ("Japan", "web")
    ]
]

TRACKS = [
    {"track_id": str(uuid.uuid4()), "track_name": track, "artist_name": artist, "genre": genre, "duration_ms": duration}
    for track, artist, genre, duration in [
        ("Blinding Lights", "The Weeknd", "Pop", 200040),
        ("HUMBLE.", "Kendrick Lamar", "Hip-Hop", 177000),
        ("Bad Guy", "Billie Eilish", "Pop", 194088),
        ("God's Plan", "Drake", "Hip-Hop", 198973),
        ("Human Nature", "Michael Jackson", "Pop", 246000),
        ("Smells Like Teen Spirit", "Nirvana", "Rock", 301920),
        ("Starboy", "The Weeknd", "R&B", 230453),
        ("Sors de ma tête", "Niro", "Rap Français", 198000),
        ("Someone Like You", "Adele", "Soul", 285000),
        ("Lose Yourself", "Eminem", "Hip-Hop", 326440),
        ("Levitating", "Dua Lipa", "Pop", 203064),
        ("Peaches", "Justin Bieber", "R&B", 198082),
        ("drivers license", "Olivia Rodrigo", "Pop", 242014),
        ("Heat Waves", "Glass Animals", "Indie", 238805),
        ("Stay", "Kid LAROI & Justin Bieber", "Pop", 141005),
    ]
]

def generate_event():
    user = random.choice(USERS) # Pioche un utilisateur au hasard dans la liste
    track = random.choice(TRACKS) # Même principe
    duration_ms = track["duration_ms"] # Récupère la durée du son pioché
    listened_ms = random.randint(int(duration_ms * 0.1), duration_ms) # elle simule le comportement d'écoute/10% de la durée = le minimum écouté (skip rapide)/100% = écoute complète/(random.randint)choisit un nombre entier aléatoire entre les deux

    
    # Résultat final de la fonction
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": user["user_id"],
        "track_id": track["track_id"],
        "track_name": track["track_name"],
        "artist_name": track["artist_name"],
        "genre": track["genre"],
        "duration_ms": duration_ms,
        "listened_ms": listened_ms,
        "timestamp": datetime.utcnow().isoformat(),
        "platform": user["platform"],
        "country": user["country"]
    }


# C'est une condition Python classique. Elle dit : "exécute ce bloc uniquement si tu lances ce fichier directement"
# Si un autre fichier importe simulator.py, ce bloc ne s'exécute pas

if __name__ == "__main__":
    import time
    print("Starting Spotify data simulator...")
    while True:
        for _ in range(10):
            event = generate_event() # génère un événement
            print(json.dumps(event)) # l'affiche en JSON
        time.sleep(1)