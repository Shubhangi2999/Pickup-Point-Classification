import boto3
import json
import SQS
import DynamoDB
import StepFunction
	
# Main function
def lambda_handler(event,context):
    response = SQS.ReceiveMsgsFromQueue() 
    store_id = DynamoDB.ComputeUniqueStoreId()
    message_body, store_id, receipt_handle = DynamoDB.InsertItemInDynamoDBTable(response, store_id)
    StepFunction.InitiateStepFunction(message_body, store_id)
    SQS.DeleteMsgsFromQueue(receipt_handle)
