from django.shortcuts import render,redirect
from .models import Chat,User,Message
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/users/login")
def chat(request):
    chats = Chat.objects.filter(participants=request.user).filter(chat_type="group")
    users = User.objects.exclude(id=request.user.id)

    return render(request,"chat.html",{'chats': chats,'users':users})

@login_required(login_url="/users/login")
def start_chat(request,user_id):
    other_user =User.objects.get(id=user_id)
    existing_chat = Chat.objects.filter(participants=request.user).filter(participants=other_user).first()

    if existing_chat:
        return redirect('chat:chat_page',slug=existing_chat.slug)

    new_chat = Chat.objects.create(chat_type="ind")
    new_chat.save()
    new_chat.add_participants(request.user,other_user)

    return redirect('chat:chat_page',slug=new_chat.slug)

@login_required(login_url="/users/login")
def chat_page(request,slug):
    chat = Chat.objects.get(slug=slug)
    users = User.objects.exclude(id=request.user.id)


    if request.user not in chat.participants.all():
        return redirect("chat:chat")

    chats = Chat.objects.filter(participants=request.user).filter(chat_type="group")
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    return render(request,'chat_page.html',{'chat':chat,'users':users,'messages':messages,'chats': chats})

# @login_required(login_url="/users/login")
# def create_group(request,slug):
#     chat = Chat.objects.get(slug=slug)