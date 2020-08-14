from django.contrib.postgres.fields import ArrayField
from django.db import models


class RestaurantMatch(models.Model):
    time_created = models.DateTimeField()
    restaurants = ArrayField(ArrayField(models.TextField()))


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    restaurant_match_id = models.ForeignKey(
        RestaurantMatch, default=None, on_delete=models.CASCADE)
