import json
import boto3

DYNAMODB = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com")
TABLE = DYNAMODB.Table('Resources-storeOnboardingData-149PFYMUWL1EF')
CLIENT = boto3.client('dynamodb')
RESULT = CLIENT.scan(TableName = "Resources-storeOnboardingData-149PFYMUWL1EF")
STORE_ID = "store_id"
PHONE_NO = "phone_no"

''' Function to scan the whole table and fetch the value 
of the maximum store id from the existing records'''
def ComputeUniqueStoreId():
	store_ids = []
	for item in RESULT['Items']:
	    for key,value in (item[STORE_ID]).items():
	        store_ids.append(int(value))
	store_id = max(store_ids)
	return store_id
	
'''function to insert a new record in the dynamodb table.
A unique store_id is assigned by incrementing the maximum value
from the previous function by 1 and status code 0 is assigned'''
def InsertItemInDynamoDBTable(response, store_id):
    msg_len = len(response['Messages'])
    for i in range(0, msg_len):
        flag = 0
        try:
            message = response['Messages'][i]
            flag = 1
        except:
            flag = 0
        
        if flag!=0 :
            receipt_handle = message['ReceiptHandle']
            message_body = message['Body']
            message_body = json.loads(message_body)
            store_id = store_id+1
            phone = message_body['phone']

            TABLE.put_item(Item = {
                'store_id': store_id,
                'name': message_body['name'],
                'phone_no': message_body['phone'],
                'email': message_body['email'],
                'location_type': message_body['location_type'],
                'location_name': message_body['location_name'],
                'city': message_body['city'],
                'open_time': message_body['open_time'],
                'close_time': message_body['close_time'],
                'disabled': message_body['disabled'],
                'visitors': message_body['visitors'],
                'owned_rented': message_body['owned_rented'],
                'store_age': message_body['store_age'],
                'staff_count': message_body['staff_count'],
                'residential': message_body['residential'],
                'address' : message_body['address'],
                'length' : message_body['length'],
                'breadth' : message_body['breadth'],
                'height' : message_body['height'],
                'working_days' : message_body['working_days'],
                'status_code': "0"
            })
    return (message_body, store_id, receipt_handle)
