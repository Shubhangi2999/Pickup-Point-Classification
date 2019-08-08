import json
import DynamoDB
import PreprocessData

'''This is the main function that calls the GetDataFromDB function
to get the data from the database, passes the data to a PreProcess function
and then send the data to the webpage for displaying it into the modal.'''
def lambda_handler(event,context):
    store_id = int(event['data'])
    item = DynamoDB.GetDataFromDB(store_id)
    data = PreprocessData.PreprocessReceivedData(item)
    return data
