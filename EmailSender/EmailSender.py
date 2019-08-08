import DynamoDB
import SendEmail

PHONE_NO = "phone_no"
EMAIL = "email"
APPLICATION_STATUS = "application_status"
STATUS_CODE = "status_code"
STATUS_ID = "4"     #status id 4 denotes that the email has been sent successfully for this applicant

'''This function returns the details of the
applicant (corresponding to the passed store ID)
that are required for sending an email.'''
def GetApplicantDetails(store_id):
    data = DynamoDB.GetDataFromDB(store_id)
    phone_no = data[PHONE_NO]['S']
    recipient = data[EMAIL]['S']
    acceptance_status = data[APPLICATION_STATUS]['S']
    return phone_no, recipient, acceptance_status

'''This is the main function that receives the applicant details
and calls the SendEmail and DynamoDb updation function.'''
def lambda_handler(event,context):
    store_id = event
    phone_no, recipient, acceptance_status  = GetApplicantDetails(store_id)
    SendEmail.SendEmail(recipient, acceptance_status)
    DynamoDB.UpdateDataInDB(store_id, phone_no, STATUS_ID, STATUS_CODE)
