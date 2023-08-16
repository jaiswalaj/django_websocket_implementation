import asyncio
import motor.motor_asyncio

from django.shortcuts import render

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client['django_websocket_db']

group_collection = db['group_collection']
chat_collection = db['chat_collection']



# Create your views here.
async def index(request, group_name):
    print("\n\nGroup Name: ", group_name, "\n\n")
    
    group = await group_collection.find_one({'group_name': group_name})
    if group:
        chat_cursor = chat_collection.find({'group_name': group_name})
        chats = await chat_cursor.to_list(None)
    else:
        # Asynchronous insert operation
        await group_collection.insert_one({'group_name': group_name})
        chats = []

    return render(request, 'chat_app/index.html', {'group_name': group_name, 'chats': chats})
