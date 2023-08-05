

# class NotificationAsyncConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         print("Websocket Connected! ", event)
#         await self.send({
#             'type': 'websocket.accept'
#         })

#     async def websocket_receive(self, event):
#         print("Message Received! ", event)
#         print("Message Received: ", event['text'])
#         await self.send({
#             'type': 'websocket.send',
#             'text': 'Async message to client'
#         })

#     async def websocket_disconnect(self, event):
#         print("Websocket Disconnected! ", event)
#         raise StopConsumer()
