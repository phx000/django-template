import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from api.ws.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

if os.environ.get("DJANGO_DEBUG"):
    application = ProtocolTypeRouter(
        {
            "http": get_asgi_application(),
            "websocket":
                AuthMiddlewareStack(
                    URLRouter(
                        websocket_urlpatterns
                    )
                )
        }
    )
else:
    application = ProtocolTypeRouter(
        {
            "websocket":
                AuthMiddlewareStack(
                    URLRouter(
                        websocket_urlpatterns
                    )
                )
        }
    )
