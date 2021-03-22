
from django.conf.urls import url,re_path
from django.core.asgi import get_asgi_application
import os
# Fetch Django ASGI application early to ensure AppRegistry is populated
# before importing consumers and AuthMiddlewareStack that may import ORM
# models.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogd.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from users import consumers


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/userschatroom/(?P<Susername>[\w@.]+)/(?P<Rusername>[\w@.]+)/$', consumers.ChatConsumer.as_asgi()),
            re_path(r'ws/notifications/$', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})