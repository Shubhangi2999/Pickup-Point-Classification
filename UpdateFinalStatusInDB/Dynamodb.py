import json
import boto3

DYNAMODB = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com")
TABLE = DYNAMODB.Table('Resources-storeOnboardingData-149PFYMUWL1EF')
CLIENT = boto3.client('dynamodb')
RESULT = CLIENT.scan(TableName = "Resources-storeOnboardingData-149PFYMUWL1EF")
STORE_ID = "store_id"
PHONE_NO = "phone_no"

'''This function updates the column (column_name)
of the database with the value (value) corresponding
to the passed store id and phone number.'''
def UpdateDataInDB(store_id, phone_no, value, column_name ):
    response = TABLE.update_item(
        Key = {
                STORE_ID : store_id,
                PHONE_NO : phone_no
            },
            UpdateExpression="set " + column_name + " = :val1",
            ExpressionAttributeValues = {
                ":val1" : value
        }
    )

'''This function retrieves and returns the record
corresponding to passed store ID'''
def GetDataFromDB( store_id ):
    store_id = int(store_id)
    for item in RESULT['Items']:
        storeid = int(item[STORE_ID]['N'])
        if(store_id == storeid):
            return item
