import sys
import json
import boto3
import requests
import os
import time
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/simulator')
sys.path.append('/opt/airflow/kafka')

MINIO_ENDPOINT = 'http://minio:9000'
MINIO_ACCESS_KEY = os.getenv('MINIO_ROOT_USER')
MINIO_SECRET_KEY = os.getenv('MINIO_ROOT_PASSWORD')
BUCKET_NAME = 'spotify-raw'

DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')
DATABRICKS_TOKEN = os.getenv('DATABRICKS_TOKEN')


def load_minio_to_volumes():
    s3_client = boto3.client(
        's3',
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY
    )

    objects = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix='events/')
    files = [obj['Key'] for obj in objects.get('Contents', [])]
    print(f"Nombre de fichiers trouvés : {len(files)}")

    for file in files:
        obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file)
        content = obj['Body'].read()

        volume_path = f"/Volumes/workspace/bronze/spotify_events/{file}"
        
        for attempt in range(3):
            try:
                response = requests.put(
                    f"{DATABRICKS_HOST}/api/2.0/fs/files{volume_path}",
                    headers={
                        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
                        "Content-Type": "application/octet-stream"
                    },
                    data=content,
                    timeout=30
                )
                if response.status_code in [200, 204]:
                    print(f"Uploaded: {volume_path}")
                    break
                else:
                    print(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2)


default_args = {
    'description': 'A DAG to orchestrate Spotify streaming pipeline',
    'start_date': datetime(2026, 7, 19),
}

with DAG(
    dag_id='spotify-streaming-orchestrator',
    default_args=default_args,
    schedule=timedelta(hours=1),
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='load_minio_to_volumes',
        python_callable=load_minio_to_volumes
    )