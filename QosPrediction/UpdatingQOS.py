import json
import os
import io
import boto3
import csv
import QosPrediction
import DynamoDB


def GetItem(store_id):
   response = DYNAMODB.GetDataFromDB(store_id)
   return response

def GetList(item):
    payload = ""
    payload += str(item['no_busstns']['N']) + ','
    payload += str(item['no_of_reviews']['S']) + ','
    payload += str(item['no_parkings']['N']) + ','
    if(item['owned_rented']['S'] == "Owned"):
        payload += str(1) + ','
    else:
        payload += str(0) + ','
    payload += str(item['rating']['S']) + ','
    payload += str(int(item['close_time']['S'][0:2]) - int(item['open_time']['S'][0:2])) + ','
    payload += str(item['staff_count']['S']) + ','
    payload += str(item['store_age']['S']) + ','
    payload += str(item['visitors']['S']) + ','
    payload += str(item['working_days']['S'])
    return payload
 

def GetPhoneNo(store_id):
   response = DynamoDB.GetDataFromDB(store_id)
   phone_no = reponse['phone_no']['S']
   return phone_no

def lambda_handler(event,context):
    store_id = event
    data = DynamoDB.GetItem(store_id)
    payload = GetList(data)
    phone_no = GetPhoneNo(store_id)
    
    pred = QosPrediction.QosPrediction(payload)    
    DynamoDB.UpdateDataInDB(store_id, phone_no, pred, 'qos')
    
    suggest = ""
    if pred>3:
        suggest = "Accept"
    else:
        suggest = "Reject" 
        
    DynamoDB.UpdateDataInDB(store_id, phone_no,suggest, 'suggest')
    DynamoDB.UpdateDataInDB(store_id, phone_no, "2", 'status_code')
    return store_id
