from django.shortcuts import render
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

#Define Db Name
dbname = client['django_websocket_db']

group_collection = dbname.get_collection("group_collection")
chat_collection = dbname.get_collection("chat_collection")


# Create your views here.
def index(request, group_name):
    print("\n\nGroup Name: ", group_name, "\n\n")
    
    
    group = group_collection.find_one({'group_name': group_name})
    if group:
        chats = chat_collection.find({'group_name': group_name})
    else:
        group_collection.insert_one({'group_name': group_name})
        chats = []

    return render(request, 'chat_app/index.html', {'group_name': group_name, 'chats': chats})
