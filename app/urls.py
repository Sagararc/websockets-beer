
from django.contrib import admin
from django.urls import path
from .views import FormData,datashow,success

urlpatterns = [

    path('' , FormData , name='form'),
    path('data/' , datashow , name='data'),
    path('success/' , success , name='success'),
]
