import json
import boto3
import os
from kafka import KafkaConsumer
from datetime import datetime, timezone

consumer = KafkaConsumer(
    'spotify-events',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest', # position du consumer
    group_id='spotify-consumer-group'
)

s3_client = boto3.client(
    's3',
    endpoint_url='http://minio:9000',
    aws_access_key_id=os.getenv('MINIO_ROOT_USER'),
    aws_secret_access_key=os.getenv('MINIO_ROOT_PASSWORD')
)

BUCKET_NAME = 'spotify-raw'

def upload_to_minio(event):
    timestamp = datetime.now(timezone.utc).strftime('%Y/%m/%d/%H')
    filename = f"events/{timestamp}/{event['event_id']}.json"
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=filename, # le chemin du fichier
        Body=json.dumps(event) # le contenu du json
    )
    print(f"Uploaded to MinIO: {filename}")

def run_consumer():
    print("Starting Kafka Consumer...")
    for message in consumer:
        event = json.loads(message.value.decode('utf-8')) # récupère le dictionnaire Python (déjà désérialisé)
        upload_to_minio(event)

if __name__ == "__main__":
    run_consumer()
