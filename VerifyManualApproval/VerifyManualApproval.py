import json
import DynamoDB

STATUS_CODE = 3

'''This function gets the status code corresponding to
the passed store id from the database.'''
def GetStatusCode(store_id):
    data = DynamoDB.GetDataFromDB(store_id)
    status_code = int(data['status_code']['S'])
    return status_code

'''This is a custom error class that is used to
raise an error if the status code of the application
corresponding to the store id isn't set to 3, i.e. manual approval
hasn't been done for it yet.'''
class CustomError(Exception):
    pass

'''The main function that checks if manual approval of an application
corresponding to the store id has been done or not and returns
the store id if it has been done, else raises a custom error.'''
def lambda_handler(event, context):
    
    store_id = event
    status_code = GetStatusCode(store_id)
    if status_code == STATUS_CODE:
        return store_id
    else:
        raise CustomError("Manual validation hasn't been done yet.")
