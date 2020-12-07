from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import users.routing

application= ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
       URLRouter(users.routing.websocaket_urlpatterns
                 )
    ),
})