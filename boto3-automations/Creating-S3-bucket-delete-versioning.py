import boto3

def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket created: {bucket_name}")

def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket deleted: {bucket_name}")

def enable_versioning(bucket_name):
    s3 = boto3.client('s3')
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"Versioning enabled on: {bucket_name}")

if __name__ == "__main__":
    bucket = "ams-rule-001-test"

    # Create bucket
    create_bucket(bucket)

    # Modify bucket
    enable_versioning(bucket)

    # Delete bucket
    delete_bucket(bucket)
