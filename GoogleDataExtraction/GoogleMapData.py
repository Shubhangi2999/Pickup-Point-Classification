import googlemaps 
import json
import boto3
import urllib2

def GetDistanceFromNearbyResidential(latitude, longitude, locname, residential):
    gmaps = googlemaps.Client(key='AIzaSyDVQuHfXijHpAuj4rEDoYfbwVJOuR-vWN4')
    distances = dict()
    for value in residential.values():
        my_distance = gmaps.distance_matrix(locname,value)['rows'][0]['elements'][0]
        distance = my_distance['distance']['text']
        distances[value] = distance
    return distances
