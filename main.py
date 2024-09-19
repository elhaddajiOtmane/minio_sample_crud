import os
from dotenv import load_dotenv
from minio import Minio
from minio.error import ResponseError

# Load environment variables from .env file
load_dotenv()

# Get MinIO credentials from environment variables
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_BUCKET = os.getenv('MINIO_BUCKET')

FILE_TO_UPLOAD = 'path/to/your/file.txt'  # Replace with the path to your file
OBJECT_NAME = 'file.txt'  # Name for the uploaded object

# Create a MinIO client
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False  # Set to True if using HTTPS
)

try:
    # Check if the bucket exists
    if not client.bucket_exists(MINIO_BUCKET):
        print(f"Bucket '{MINIO_BUCKET}' does not exist. Creating bucket...")
        client.make_bucket(MINIO_BUCKET)
    
    # Upload the file
    client.fput_object(MINIO_BUCKET, OBJECT_NAME, FILE_TO_UPLOAD)
    print(f"File '{FILE_TO_UPLOAD}' uploaded to bucket '{MINIO_BUCKET}' as '{OBJECT_NAME}'.")
except ResponseError as err:
    print(f"An error occurred: {err}")