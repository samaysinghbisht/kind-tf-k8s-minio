import os
from minio import Minio
from minio.error import S3Error


# MinIO server configuration
minio_host = os.getenv("MINIO_HOST")  # DNS name of the MinIO service in infra cluster

# Create a MinIO client
minio_client = Minio(
    minio_host,
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)

def create_bucket(bucket_name):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except S3Error as err:
         print(f"Error: {err}")


# Upload images from the local directory to the Minio bucket
def upload_images(bucket_name):
    try:
        for filename in os.listdir("images"):
            if filename.endswith((".jpeg", ".webp")):
                object_name = filename
                file_path = os.path.join("images", filename)
                minio_client.fput_object(bucket_name, object_name, file_path)
        return True
    except S3Error as err:
        print(err)
        return False

if __name__ == "__main__":
    bucket_name = "justwatch"
    create_bucket(bucket_name)
     # Upload images to the bucket
    upload_images(bucket_name)
