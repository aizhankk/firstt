from django.contrib import admin

# Register your models here.


from .models import Room, Genre, Message

admin.site.register(Room)

admin.site.register(Genre)

admin.site.register(Message)

