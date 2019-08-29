from django.contrib import admin
from django.urls import path,include

from .views import DoctorList,DoctorDetail

app_name = 'doctor'
urlpatterns = [
    path('',DoctorList.as_view(), name = 'home' ),
    path('doctor/<int:pk>/',DoctorDetail.as_view(), name = 'doctor_detail' ),
    
]
