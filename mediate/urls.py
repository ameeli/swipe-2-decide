from django.urls import path

from . import views

urlpatterns = [
    path('api/mediate/', views.ListRestaurants.as_view()),
]
