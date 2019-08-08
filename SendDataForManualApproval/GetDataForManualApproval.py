import json
import boto3

CLIENT = boto3.client('dynamodb')
RESULT = CLIENT.scan(TableName = "Resources-storeOnboardingData-149PFYMUWL1EF")
STORE_ID = "store_id"
STATUS_CODE = "status_code"

'''This function creates the list of data that needs
to be sent to the webpage to be dislayed in the table.'''
def createList(item):
    table_data = list()
    table_data.append(item[STORE_ID]['N'])
    table_data.append(item['name']['S']) 
    table_data.append(item['location_name']['S'])
    table_data.append(item['location_type']['S'])
    table_data.append(item['city']['S'])
    return table_data	

'''This function gets the data from the database
which has the status code that is passed to the function.'''
def GetDataForStatusCode(status_id):
    data_list = list()
    for item in RESULT['Items']:
        store_id = item[STORE_ID]['N']
        status_code = int(item[STATUS_CODE]['S'])
        if(store_id != 0 and status_code == status_id):
            tableData = createList(item)
            data_list.append(tableData)
    return data_list
    
