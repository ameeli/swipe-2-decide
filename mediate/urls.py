from django.urls import path

from . import views

urlpatterns = [
    path('api/find_restaurants/', views.FindRestaurants.as_view()),
]
