import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "game_%s" % self.room_name
        
        #IDK session
        self.scope["session"]["seed"] = random.randint(1,1000)
        
        print(self.scope["session"])
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        host = text_data_json.get('host')
        player = text_data_json.get('player')
        p_status = text_data_json.get('p_status')
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, "host": host, "player":player, "p_status": p_status, }

        )
        await sync_to_async(self.scope["session"].save)()

    # Receive message from room group
    async def chat_message(self, event):
        message = event.get("message")
        host = event.get('host')
        player = event.get('player')
        p_status = event.get('p_status')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "host": host, "player": player, 'p_status': p_status}))
