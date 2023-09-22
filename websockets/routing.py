from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
    re_path(r'ws/ac/', consumers.MyAsyncConsumer.as_asgi()),
]
