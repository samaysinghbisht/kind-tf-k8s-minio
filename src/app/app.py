import os
from flask import Flask, render_template, send_file, request
from minio import Minio

app = Flask(__name__)

minio_host = os.getenv("MINIO_HOST") 
# Initialize the Minio client
minio_client = Minio(
    minio_host,  # Replace with the Minio service DNS or IP
    access_key=os.getenv("MINIO_ACCESS_KEY"),  # Replace with your Minio access key
    secret_key=os.getenv("MINIO_SECRET_KEY"),  # Replace with your Minio secret key
    secure=False,  # Set to True if your Minio server uses HTTPS
)

@app.route("/")
def index():
    # Replace 'justwatch' with your Minio bucket name
    bucket_name = "justwatch"

    # List objects in the bucket
    objects = minio_client.list_objects(bucket_name)

    # Get the list of image URLs
    image_urls = [minio_client.presigned_get_object(bucket_name, obj.object_name) for obj in objects]

    return render_template("index.html", image_urls=image_urls)

if __name__ == "__main__":
    app.run(debug=True)
    