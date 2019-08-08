import json
import boto3

STEP_FUNCTION_CLIENT = boto3.client('stepfunctions')

# Initiate first stage of the step function i.e. Google data Extraction
def InitiateStepFunction(message_body, store_id):
    google_data = {
        'input': {
            'residential': message_body['residential'],
            'store_id': store_id,
            'phone_no': message_body['phone'],
            'location_name': message_body['location_name'],
            'location_type': message_body['location_type'],
            'address': message_body['address']
        }
    }
    google_data=json.dumps(google_data)
    response_from_step_fn_client = STEP_FUNCTION_CLIENT.start_execution(stateMachineArn='arn:aws:states:us-east-2:060708593102:stateMachine:ApplicationProcessingFlow-wvYSANtQMXxx', input = google_data)
