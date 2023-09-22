from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path(r'ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
]
