from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        self.chat_room_id = self.scope['path_remaining']
        self.thread_name = f"chat_room_{self.chat_room_id}"
        print(self.thread_name)
        await self.channel_layer.group_add(
            self.thread_name,
            self.channel_name
        )

        await self.accept()

    async def websocket_receive(self, event):
        print("Message: ", event['text'])

        await self.channel_layer.group_send(
            self.thread_name,
            {
                "type": "send.message",
                "data": event['text']
            }
        )

    async def send_message(self, event):
        print('messages', event)
        await self.send_json(event['data'])

    async def websocket_disconnect(self, event):
        print("disonnected", event)
        await self.channel_layer.group_discard(
            self.thread_name,
            self.channel_name
        )
        await self.disconnect(event['code'])
        raise StopConsumer()

    @database_sync_to_async
    def fetch_device_data(self):
        pass


