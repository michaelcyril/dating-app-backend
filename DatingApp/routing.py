from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from social_management.consumers import ChatRoomConsumer

application = ProtocolTypeRouter({
    #Empty
    #"http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
                URLRouter(
                [
                    # re_path(r"^student-fprint-socket-portal", StudentRegPortal_Consumer.as_asgi()),
                    # re_path(r"^student-attendance-socket-portal", AttPortal_Consumer.as_asgi()),
                    re_path(r"^chat-room-conversation/(?P<chat_id>)", ChatRoomConsumer.as_asgi()),
                    #url(r"^user-notifications-portal/(?P<deviceNo>)", User_Dev_Portal.as_asgi()),
                ]
            )
        )
    )
})