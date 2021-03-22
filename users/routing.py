from django.urls import re_path
from . import consumers
print("in routing ---")
websocaket_urlpatterns=[
    re_path(r'ws/userschatroom/(?P<Susername>[\w@.]+)/(?P<Rusername>[\w@.]+)/$',consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/notifications/$', consumers.ChatConsumer.as_asgi()),
]