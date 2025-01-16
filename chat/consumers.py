import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import Chat, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_slug = self.scope['url_route']['kwargs']['chat_slug']
        self.room_group_name = f'chat_{self.chat_slug}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope['user'].id
        username = self.scope['user'].username

        await self.save_message(user_id,message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':message,
                'username':username,
                'timestamp':timezone.now().isoformat(),
            }
        )

    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
            'message':event['message'],
            'username':event['username'],
            'timestamp':event['timestamp'],


        }))

    @database_sync_to_async
    def save_message(self,user_id,message):
        chat = Chat.objects.get(slug=self.chat_slug)
        Message.objects.create(
            chat=chat,
            sender_id=user_id,
            content=message
        )