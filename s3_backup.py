"""
this is script to take a backup from local to AWS S3
boto3 -> used to do AWS tasks using python 
"""

import boto3
import datetime

# Generate a unique bucket name
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
bucket_name = f"python-for-devops-junoon-kashif-{timestamp}"

# Create S3 resource
s3 = boto3.resource("s3", region_name="eu-west-1")

# Create bucket
def create_bucket(s3_resource, bucket_name):
    s3_resource.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1'
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")

# Show all buckets
def show_buckets(s3_resource):
    print("Your buckets:")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

# Upload a file to the created bucket
def upload_file_to_bucket(s3_resource, bucket_name, file_name, object_name=None):
    if object_name is None:
        object_name = file_name  # use local filename as object key
    try:
        s3_resource.Bucket(bucket_name).upload_file(file_name, object_name)
        print(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

create_bucket(s3, bucket_name)
show_buckets(s3)

# File to upload (adjust path and name as needed)
file_to_upload = "test_upload.txt"  # put your file name here
upload_file_to_bucket(s3, bucket_name, file_to_upload)
