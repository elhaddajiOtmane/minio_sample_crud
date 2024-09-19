from minio import Minio
from minio.error import ResponseError

# Replace with your MinIO credentials and endpoint
MINIO_ENDPOINT = 'http://18.153.64.112:9000'
MINIO_ACCESS_KEY = 'ROOTNAME'
MINIO_SECRET_KEY = 'CHANGEME123'
MINIO_BUCKET = 'astucepro'
FILE_TO_UPLOAD = 'path/to/your/file.txt' 
OBJECT_NAME = 'file.txt'  

# Create a MinIO client
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False  
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
