import json
import boto3
import GetDataForManualApproval

STATUS_CODE = 2

'''The main function that calls the GetDataForStatusCode function
to get the data corresponding to a specific store id.'''
def lambda_handler(event, context):
    manual_approval_data = GetDataForManualApproval.GetDataForStatusCode(STATUS_CODE)
    return manual_approval_data
