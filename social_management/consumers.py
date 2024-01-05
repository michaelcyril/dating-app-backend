from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        # print(self.scope['path_remaining'])
        print(self.scope)
        self.chat_room_id = self.scope['path_remaining']
        self.thread_name = f"chat_room_{self.chat_room_id}"
        print(self.thread_name)
        await self.channel_layer.group_add(
            self.thread_name,
            self.channel_name
        )
        # OnlineUpdate(True, self.deviceNo)
        # print('ll')

        await self.accept()
        # await self.fetch_device_data()
        # await self.send_json(self.)

    async def websocket_receive(self, event):
        print("Message: ", event['text'])

        await self.channel_layer.group_send(
            "thread_1",
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
        # OnlineUpdate(False, self.deviceNo)
        await self.channel_layer.group_discard(
            self.thread_name,
            self.channel_name
        )
        await self.disconnect(event['code'])
        raise StopConsumer()

    @database_sync_to_async
    def fetch_device_data(self):
        pass
        # print(self.deviceNo)
        # data = MongoDevicesManagement().getUserDevice({"deviceNo": self.deviceNo})
        # print(data)
        # self.device_data = json.loads(json_util.dumps(data))


