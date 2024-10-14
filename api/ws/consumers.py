from channels.generic.websocket import AsyncWebsocketConsumer
import json


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.session_id = self.scope["url_route"]["kwargs"]["session_id"].replace("-", "")
        # await self.channel_layer.group_add(self.session_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # await self.channel_layer.group_discard(self.session_id, self.channel_name)
        return

    async def receive(self, text_data):
        # data = json.loads(text_data)
        #
        # await self.channel_layer.group_send(
        #     self.session_id, {"type": "send.data", "data": "data"}
        # )
        return

    async def send_data(self, event):
        # data = event["data"]

        # await self.send(text_data=json.dumps({"data": data}))
        return