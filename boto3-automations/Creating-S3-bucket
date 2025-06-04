import boto3

def lamda_handler(event, context):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket = 'ams_rule_001')
    return{
        'status' : 200,
        'body' : 's3 bucket enabled!'
    }
