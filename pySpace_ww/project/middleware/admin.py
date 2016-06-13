from django.contrib import admin

# Register your models here.
from .models import User, Message, Choice

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Choice)