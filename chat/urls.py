from django.contrib import admin
from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('',views.chat,name="chat"),
    path('start/<int:user_id>',views.start_chat,name="start_chat"),
    path('<slug:slug>',views.chat_page,name="chat_page"),

]