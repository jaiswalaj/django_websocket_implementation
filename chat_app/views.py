from django.shortcuts import render

# Create your views here.
def index(request, group_name):
    print("\n\nGroup Name: ", group_name, "\n\n")
    return render(request, 'chat_app/index.html', {'group_name': group_name})
