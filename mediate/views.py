from rest_framework.views import APIView
from rest_framework.response import Response

from mediate.utils.access_yelp import get_restaurants

temp = [
    {'id': 1, 'name': 'cafe', 'stars': 4, 'price': 2, 'review_count': 100},
    {'id': 2, 'name': 'diner', 'stars': 3, 'price': 1, 'review_count': 200},
    {'id': 3, 'name': 'bakery', 'stars': 5, 'price': 3, 'review_count': 50}
]


class FindRestaurants(APIView):
    def get(self, request, format=None):
        # price_range = request.POST['price_range']
        # response = requests.get('https://ipinfo.io/json')
        # location_data = json.loads(response.text)

        # restaurants = get_restaurants(price_range, location_data)
        return Response(temp)
