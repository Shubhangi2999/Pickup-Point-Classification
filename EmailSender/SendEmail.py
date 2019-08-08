import json
import boto3
from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"    #us-east-1 is one of the regions where SES service is supported
CLIENT = boto3.client('ses',region_name=AWS_REGION)
SENDER = "Amazon Locker <locker-onboarding@amazon.com>"
SUBJECT = "Amazon Locker Setup."
CHARSET = "UTF-8"

'''This function returns the mail content to be sent
as per the user's application acceptance status.'''
def GetBody(acceptance_status):
    
    if(acceptance_status == 'Accepted'):
        BODY_HTML = """
            <html>
            <head></head>
            <body>
                <p> Your application for locker installation has been accepted! </p>
            </body>
            </html> 
        """
    else:
        BODY_HTML = """
            <html>
            <head></head>
            <body>
                <p> your request has been rejected! </p>
            </body>
            </html> 
        """  
    return BODY_HTML

'''This function deals with binding the email components
and finally sending the email.'''
def SendEmail(recepient, acceptance_status):
    body_html = GetBody(acceptance_status)
          
    try:
        response = CLIENT.send_email(
            Destination = {
                'ToAddresses': [
                    recepient,
                ],
            },
            Message = {
                'Body':{
                    'Html':{
                        'Charset': CHARSET,
                        'Data': body_html
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source = SENDER
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:")
        print(response['MessageId'])
