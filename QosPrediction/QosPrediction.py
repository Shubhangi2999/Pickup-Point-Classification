import json
import os
import io
import boto3
import csv

ENDPOINT_NAME = os.environ['ENDPOINT_NAME'] #Accessing the endpoint created through sagemaker notebook
RUNTIME = boto3.client('runtime.sagemaker') #creating a sagemaker runtime

def QosPrediction(payload):
    response = RUNTIME.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='text/csv', Body = payload) 
    result = json.loads(response['Body'].read().decode())
    prediction = int(result['predictions'][0]['score'])
    
    if prediction < 0:
        prediction = 0
    elif prediction > 5:
        prediction = 5
    return prediction
