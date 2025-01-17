from django.db import models
from django.contrib.auth.models import User,AbstractUser
import uuid
import random 
import string
# class User(AbstractUser):
#     userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.CharField(max_length=35, unique=True)
#     profilePic = models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    
#     def __str__(self):
#         return self.username
        

#     profilePic = models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    
#     def __str__(self):
#         return self.username
        

class Chat(models.Model):
    chatid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)
    chat_type = models.TextField(default='group')
    title = models.TextField(default="__default__")
    slug = models.SlugField(unique=True)

    def generate_random_slug(self):
        length = 8
        charset = string.ascii_lowercase + string.digits
        random_slug = ""
        while Chat.objects.filter(slug=random_slug).exists():
            random_slug = "".join(random.choices(charset,k=length))
        return random_slug

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = self.generate_random_slug()

        super().save(*args,**kwargs)

    def update_title(self,title=None):

        if self.title == "__default__" and not title:
            particpant_names= ",".join(user.username for user in self.participants.all())
            self.title = f"Chat between: {particpant_names}"
            self.save(update_fields=["title"])

    def add_participants(self,*users):
        super().save()
        for user in users:
            self.participants.add(user)
        self.update_title()

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.chat.title} at {self.timestamp}"