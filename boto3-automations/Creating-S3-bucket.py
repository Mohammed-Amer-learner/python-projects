import boto3

def lambda_handler(event=None, context=None):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket='ams-rule-001')  # bucket names must not have underscores
    return {
        'status': 200,
        'body': 'S3 bucket enabled!'
    }

if __name__ == "__main__":
    response = lambda_handler()
    print(response)

#output : {'status': 200, 'body': 'S3 bucket enabled!'}
