import json
import boto3
import urllib2
import GoogleDataExtraction
import DynamoDB
import GoogleMapData

def lambda_handler(event,context):
    store_id = event['input']['store_id']
    phone_no = event['input']['phone_no']
    residential = event['input']['residential']
    address = event['input']['address']
    loctype = event['input']['location_type']
    locname = event['input']['location_name']
    latitude , longitude , place_id , content = GoogleDataExtraction.GetPlaceid(locname , address)
    
    if(!latitude):
        DynamoDB.DeleteFromDB(store_id , phone_no)
    else:
        ratings = GoogleDataExtraction.GetRatings(content , latitude , longitude)
        DynamoDB.UpdateDataInDB(store_id , phone_no , ratings , 'rating')
        
        no_of_parkings = GoogleDataExtraction.GetNoOfParkings(latitude , longitude)
        DynamoDB.UpdateDataInDB(storeid , phoneno , no_of_parkings , 'no_parkings')
        
        no_of_busstns = GoogleDataExtraction.GetNoOfBusstns(latitude , longitude)
        DynamoDB.UpdateDataInDB(store_id , phone_no , no_of_busstns , 'no_busstns')
        
        no_of_reviews = GoogleDataExtraction.GetNoOfReviews(latitude , longitude)
        DynamoDB.UpdateDataInDB(store_id , phone_no , no_of_reviews , 'no_of_user_reviews')
        
        distances = GoogleMapData.GetDistanceFromNearbyResidential(latitude , longitude , locname , residential)
        DynamoDB.UpdateDataInDB(store_id , phone_no , distances , 'distance_from_residential')
        
        DynamoDB.UpdateDataInDB(store_id , phone_no , '1' , 'status_code')
        
        return storeid
