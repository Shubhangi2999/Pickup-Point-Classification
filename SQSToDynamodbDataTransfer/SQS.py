import json
import boto3

SQS = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/060708593102/Resources-storeOnboardingApplicationsQueue-1MBWXS2UAD6BY'

# Receive messages from the SQS
def ReceiveMsgsFromQueue():
	response = SQS.receive_message(
        QueueUrl = QUEUE_URL,
        AttributeNames = ['All'],
        MaxNumberOfMessages = 10,
        VisibilityTimeout = 30,
        WaitTimeSeconds = 20
    )
	return response
	
''' Delete message from the SQS after step function for
that message has been initiated'''
def DeleteMsgsFromQueue(receipt_handle):
	SQS.delete_message(
        QueueUrl = QUEUE_URL,
        ReceiptHandle = receipt_handle
    )
