import googlemaps 
import json
import boto3
import urllib2

def GetPlaceid(locname, address):
    placeid_query = locname
    place = placeid_query.split(" ")
    placeid_query = place[0]
    
    for i in place[1:]:
        placeid_query = placeid_query + "%20" + i
    
    placeid_query2 = address
    place2 = placeid_query2.split(" ")
    placeid_query2 = place2[0]
    
    for j in place2[1:]:
        placeid_query2 = placeid_query2 + "%20" + j
        
    placeid_query = placeid_query + "%20" + placeid_query2
    
    placeid_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + placeid_query + "&inputtype=textquery&fields=place_id,rating,geometry&key=AIzaSyDVQuHfXijHpAuj4rEDoYfbwVJOuR-vWN4"
    request = urllib2.Request(placeid_url, headers = {'User-Agent' : "Magic Browser"})
    file = urllib2.urlopen(request)
    content = file.read()
    content = json.loads(content)
    try:
        content = content['candidates'][0]
    except:
        return
        
    latitude = str(content['geometry']['location']['lat'])
    longitude = str(content['geometry']['location']['lng'])
    place_id = content['place_id']
    
    return latitude,longitude,place_id,content

def GetRatings(content, lat, lng):
    try:
        rating = str(content['rating'])
        return rating
    except:
        return "0"

def GetNoOfParkings(lat, lng):
    parking_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "," + lng + "&radius=1000&type=parking&key=AIzaSyDVQuHfXijHpAuj4rEDoYfbwVJOuR-vWN4"
    request = urllib2.Request(parking_url, headers = {'User-Agent' : "Magic Browser"})
    file = urllib2.urlopen(request)
    content = file.read()
    content = json.loads(content)
    try:
        parking_count = len(content["results"])
        return parking_count
    except:
        return 0

def GetNoOfBusstns(lat, lng):
    bus_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "," + lng + "&radius=200&type=bus_station&key=AIzaSyDVQuHfXijHpAuj4rEDoYfbwVJOuR-vWN4"
    request = urllib2.Request(bus_url, headers = {'User-Agent' : "Magic Browser"})
    file = urllib2.urlopen(request)
    content = file.read()
    content = json.loads(content)
    try:
        bus_count = len(content["results"])
        return bus_count
    except:
        return 0

def GetNoOfReviews(lat, lng):
    reviews_url="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "," + lng + "&radius=3&type=" + loctype + "&key=AIzaSyDVQuHfXijHpAuj4rEDoYfbwVJOuR-vWN4"
    try:
        request = urllib2.Request(reviews_url, headers={'User-Agent' : "Magic Browser"})
        file = urllib2.urlopen(request)
        content = file.read()
        content = json.loads(content)
        try:
            no_of_user_reviews=content['results'][0]['user_ratings_total']
            return no_of_user_reviews
        except:
            return 0
    except:
        return 0

