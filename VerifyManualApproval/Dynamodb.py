import json
import boto3


CLIENT = boto3.client('dynamodb')
RESULT = CLIENT.scan(TableName = "Resources-storeOnboardingData-149PFYMUWL1EF")
STORE_ID = "store_id"
PHONE_NO = "phone_no"

'''This function retrieves and returns the record
corresponding to passed store ID'''
def GetDataFromDB( store_id ):
    store_id = int(store_id)
    for item in RESULT['Items']:
        storeid = int(item[STORE_ID]['N'])
        if(store_id == storeid):
            return item
