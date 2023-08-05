from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<slug:group_name>/', consumers.ChatSyncConsumer.as_asgi()),
    path('ws/ac/<slug:group_name>/', consumers.ChatAsyncConsumer.as_asgi()),
]