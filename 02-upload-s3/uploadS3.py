import boto3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python uploadS3.py <bucket name> <object name> <source file>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    object_name = sys.argv[2]
    source_file = sys.argv[3]

    s3 = boto3.client('s3')
    with open(source_file, "rb") as f:
        s3.upload_fileobj(f, bucket_name, object_name)