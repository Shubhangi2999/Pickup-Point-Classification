import json
import DynamoDB

APPLICATION_STATUS = "application_status"
STATUS_CODE = "status_code"
STATUS_ID = "3"     #status code 3 signifies that the manual approval for an application has been completed and the final acceptance status has been updated in the database
PHONE_NO = "phone_no"

'''This function gets the phone no for the applicant
corresponding to the passed store id.'''
def GetPhoneNo(store_id):
    data = DynamoDB.GetDataFromDB(store_id)
    phone_no = data[PHONE_NO]['S']
    return phone_no

'''This function updates the final acceptance status of an application
in the database and sets its status code to 3.'''
def lambda_handler(event, context):
    
    data = event["data"]
    data = json.loads(data)
    store_id = int(data["store_id"])
    status_ar = ""
    phone_no = GetPhoneNo(store_id)
    
    if(int(data["status_ar"]) == 1):
        status_ar = "Accepted"
    else:
        status_ar = "Rejected"
        
    DynamoDB.UpdateDataInDB(store_id, phone_no, status_ar, APPLICATION_STATUS)
    DynamoDB.UpdateDataInDB(store_id, phone_no, STATUS_ID, STATUS_CODE)
    
    return "Application " + status_ar + "."
