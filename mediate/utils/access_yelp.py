import os
import requests

API_HOST = 'https://api.yelp.com/v3'
BUSINESS_SEARCH = '/businesses/search'
SEARCH_PATH = '{}{}'.format(API_HOST, BUSINESS_SEARCH)
API_KEY = os.environ['YELP_API_KEY']
API_KEY_PREFACE = 'Bearer '


def get_restaurants(price_range, location_data):
    lat, long = location_data['loc'].split(',')

    headers = {'Authorization': '{}{}'.format(API_KEY_PREFACE, API_KEY)}
    params = {
        'latitude': lat,
        'longitude': long,
        'categories': 'Restaurants',
        'price': price_range
    }

    restaurants = requests.get(SEARCH_PATH,
                               headers=headers,
                               params=params)
    business_list = get_essential_info(restaurants.json()['businesses'])

    return business_list


def get_essential_info(business_list):
    ess_info = {}

    for business in business_list:
        ess_info[business['name']] = {
            'review_count': business['review_count'],
            'rating': business['rating'],
            'is_open': not business['is_closed'],
            'yelp_page': business['url'],
        }

    return ess_info
