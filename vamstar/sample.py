import json
import boto3
import time

s3 = boto3.client('s3')
def lambda_handler(event, context):
    bucket ='manojkumar-sample-s3'
    fileName = 'sample1' + '.txt'
    uploadByteStream = bytes(json.dumps(event).encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)
    print('Put Complete')
