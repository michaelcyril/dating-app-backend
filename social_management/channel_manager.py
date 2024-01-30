from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from bson import json_util
import json


class PostToChatChannel:
    def __init__(self, data):
        print(data)
        self.channel_name, self.data = f"chat_room_{data['conversation_id']}", data
        print(self.channel_name)
        self.post_to_channel()

    def post_to_channel(self):
        layer = get_channel_layer()
        print("KKKK")
        async_to_sync(layer.group_send)(self.channel_name, {
            "type": "send.message",
            "data": json.loads(json.dumps(self.data))
            # "data": json.loads(json_util.dumps(self.data))
        })


