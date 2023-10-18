
from django.contrib import admin
from django.urls import path,include
from app.views import FormData,datashow,success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('' , FormData , name='form'),
    path('data/' , datashow , name='data'),
    path('success/' , success , name='success'),
]
