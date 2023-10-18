
from django.contrib import admin
from django.urls import path,include
from .views import FormData,datashow

urlpatterns = [

    path('' , FormData , name='form'),
    path('data/' , datashow , name='data')
]
