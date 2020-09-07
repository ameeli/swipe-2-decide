import unittest

from mediate.utils.access_yelp import get_essential_info

business_list = [
    {'id': 'id1',
     'alias': 'biz1',
     'name': 'Business One',
     'image_url': 'non-essentail info',
     'is_closed': False,
     'url': 'https://www.yelp.com/biz/1',
     'review_count': 714,
     'categories': [
        {'alias': 'creperies', 'title': 'Creperies'},
        {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'},
        {'alias': 'sandwiches', 'title': 'Sandwiches'}],
     'rating': 4.0,
     'coordinates': {'latitude': 38.24853, 'longitude': -122.04423},
     'transactions': ['pickup', 'delivery'],
     'price': '$$',
     'location': {
        'address1': 'Street 1',
        'address2': '',
        'address3': '',
        'city': 'Cityone',
        'zip_code': '11111',
        'country': 'US',
        'state': 'CA',
        'display_address': ['Street 1', 'Cityone, CA 11111']},
     'phone': '+11111111111',
     'display_phone': '(111) 111-1111',
     'distance': 382.6052039057795},
    {'id': 'id2',
     'alias': 'biz2',
     'name': 'Business Two',
     'image_url': 'non-essentail info',
     'is_closed': True,
     'url': 'https://www.yelp.com/biz/2',
     'review_count': 8925,
     'categories': [
        {'alias': 'creperies', 'title': 'Creperies'},
        {'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch'},
        {'alias': 'sandwiches', 'title': 'Sandwiches'}],
     'rating': 4.6,
     'coordinates': {'latitude': 38.24853, 'longitude': -222.04423},
     'transactions': ['pickup', 'delivery'],
     'price': '$',
     'location': {
        'address1': 'Street 2',
        'address2': '',
        'address3': '',
        'city': 'Citytwo',
        'zip_code': '22222',
        'country': 'US',
        'state': 'CA',
        'display_address': ['Street 2', 'Citytwo, CA 22222']},
     'phone': '+22222222222',
     'display_phone': '(222) 222-2222',
     'distance': 382.6052039057795},
]


class TestRestaurants(unittest.TestCase):
    def setUp(self):
        self.business_list = business_list
        self.ess_info = [
            {
                'id': 'id1',
                'name': 'Business One',
                'review_count': 714,
                'rating': 4,
                'is_open': True,
                'yelp_page': 'https://www.yelp.com/biz/1'
            },
            {
                'id': 'id2',
                'name': 'Business Two',
                'review_count': 8925,
                'rating': 4.6,
                'is_open': False,
                'yelp_page': 'https://www.yelp.com/biz/2'
            },
        ]

    def test_get_essential_info(self):
        ess_info = get_essential_info(self.business_list)
        self.assertEqual(ess_info, self.ess_info)
