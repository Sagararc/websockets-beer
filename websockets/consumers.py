
import json
from channels.generic.websocket import AsyncWebsocketConsumer

import asyncio

class ContactConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        # Simulate a delay of 15 seconds
        await asyncio.sleep(5)

        await self.send(text_data=json.dumps({
            'message': message
        }))
