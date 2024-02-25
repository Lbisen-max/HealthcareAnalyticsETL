import boto3
from io import StringIO

def upload_file_to_s3(local_file_path,bucket_name,s3_file_key,aws_access_key, aws_secret_key):
    try:
        # Initialize S3 client
        s3_client = boto3.resource(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            service_name='s3'
        )
        # Upload file to S3 bucket
        s3_client.Bucket(bucket_name).upload_file(local_file_path, s3_file_key)
        print("File uploaded successfully to S3 bucket:", bucket_name, "with key:", s3_file_key)
    except Exception as e:
        print("Error:", e)





