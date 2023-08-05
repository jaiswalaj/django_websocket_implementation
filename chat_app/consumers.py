from channels.generic.websocket import AsyncWebsocketConsumer, SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

from .views import group_collection, chat_collection


class ChatSyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("\n\nWebsocket Connected! ", event)
        print("Channel Layer... ", self.channel_layer)
        print("Channel Name... ", self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['group_name']
        print("Group Name: ", self.group_name)

        # Since this group_add function is a asynchronous function and we are using it inside a Synchronous consumer so we have to add 
        # async_to_sync function to make it synchronous here.
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("\n\nMessage Received! ", event)
        print("Message Received: ", event['text'])
        # self.send({
        #     'type': 'websocket.send',
        #     'text': 'Message to client'
        # })
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print('Chat Message Handler Event: ', event)
        print('Chat Message Handler Actual Message: ', event['message'])
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })


    def websocket_disconnect(self, event):
        print("\n\nWebsocket Disconnected! ", event)
        print("Channel Layer... ", self.channel_layer)
        print("Channel Name... ", self.channel_name)

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, 
            self.channel_name
        )

        raise StopConsumer()



class ChatAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("\n\nWebsocket Connected! ", event)
        print("Channel Layer... ", self.channel_layer)
        print("Channel Name... ", self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['group_name']
        print("Group Name: ", self.group_name)

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("\n\nMessage Received! ", event)
        print("Message Received: ", event['text'])

        chat_data = json.loads(event['text'])
        group = group_collection.find_one({'group_name': self.group_name})

        new_chat = {
            'content': chat_data['msg'],
            'group_name': group['group_name']
        }
        chat_collection.insert_one(new_chat)

        await self.channel_layer.group_send(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        })

    async def chat_message(self, event):
        print('Chat Message Handler Event: ', event)
        print('Chat Message Handler Actual Message: ', event['message'])
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })


    async def websocket_disconnect(self, event):
        print("\n\nWebsocket Disconnected! ", event)
        print("Channel Layer... ", self.channel_layer)
        print("Channel Name... ", self.channel_name)

        await self.channel_layer.group_discard(self.group_name, self.channel_name)

        raise StopConsumer()
