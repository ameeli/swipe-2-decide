from rest_framework.views import APIView
from rest_framework.response import Response

temp = [
    {'id': 1, 'name': 'cafe', 'stars': 4, 'price': 2, 'review_count': 100},
    {'id': 2, 'name': 'diner', 'stars': 3, 'price': 1, 'review_count': 200},
    {'id': 3, 'name': 'bakery', 'stars': 5, 'price': 3, 'review_count': 50}
]


class ListRestaurants(APIView):
    def get(self, request, format=None):
        return Response(temp)
