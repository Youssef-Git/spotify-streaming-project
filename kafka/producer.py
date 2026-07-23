import json
import time
from kafka import KafkaProducer
import sys
#sys.path.append('/opt/airflow/simulator')
sys.path.append('/app/simulator')
from simulator import generate_event

# Se connecte au broker kafka sur le port 9092
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8') # convertit le dict Python en JSON encodé en bytes (Kafka ne travaille qu'avec des bytes)
)

def run_producer():
    print("Starting Kafka Producer...")
    while True:
        for _ in range(10):
            event = generate_event()
            producer.send('spotify-events', value=event) # envoie l'événement dans le topic spotify-events
            print(f"Event sent: {event['track_name']} - {event['artist_name']}")
        time.sleep(1)

if __name__ == "__main__":
    run_producer()