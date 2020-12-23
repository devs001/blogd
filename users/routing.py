from django.urls import re_path
from . import consumers
print("here---")
websocaket_urlpatterns=[
    re_path(r'ws/userschatroom/(?P<Susername>\D+)/(?P<Rusername>\D+)/$',consumers.ChatConsumer.as_asgi()),

]