from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import  rating_create

app_name = 'rating'
urlpatterns = [
    path('create/', login_required(rating_create), name = 'create_rating' ), 
]
