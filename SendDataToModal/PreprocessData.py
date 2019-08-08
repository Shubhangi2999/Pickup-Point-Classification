import json 

'''This function preprocess the data before sending
it to the caller function (i.e. removing 'S', 'N' etc keys
that denote whether the value is a string or a number.'''
def PreprocessReceivedData(item):
    data = dict()
    data['location_name'] = item['location_name']['S']
    data['location_type'] = item['location_type']['S']
    data['phone_no'] = item['phone_no']['S']
    data['address'] = item['address']['S']
    data['city'] = item['city']['S']
    data['area_dimensions'] = item['area_dimensions']['S']
    data['open_time'] = item['open_time']['S']
    data['close_time'] = item['close_time']['S']
    data['disabled'] = item['disabled']['S']
            
    pair = dict()
    for key,value in item['distance_from_residential']['M'].items():
        pair[key] = value['S']
    data['distance_from_residential'] = pair
    
    data['email'] = item['email']['S']
    data['name'] = item['name']['S']
    data['no_busstns'] = item['no_busstns']['N']
    data['no_of_reviews'] = item['no_of_reviews']['S']
    data['no_parkings'] = item['no_parkings']['N']
    data['owned_rented'] = item['owned_rented']['S']
    data['rating'] = item['rating']['S']
    data['staff_count'] = item['staff_count']['S']
    data['store_age'] = item['store_age']['S']
    data['visitors'] = item['visitors']['S']
    data['working_days'] = item['working_days']['S']
    data['suggest'] = item['suggest']['S']
    data['qos'] = item['qos']['N']
    
    return data
