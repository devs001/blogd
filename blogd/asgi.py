"""
ASGI config for blogd project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import re_path
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogd.settings')
from channels.auth import AuthMiddlewareStack
from ..users import consumers
application = get_asgi_application()

application=ProtocolTypeRouter(
        {
            'websocket': AuthMiddlewareStack(
                URLRouter([
                    re_path(r'ws/userschatroom/(?P<Susername>[\w@.]+)/(?P<Rusername>[\w@.]+)/$',consumers.ChatConsumer.as_asgi()),
                    re_path(r'ws/notifications/$', consumers.ChatConsumer.as_asgi()),
                ])
            ),
        }
)