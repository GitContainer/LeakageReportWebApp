from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    location = models.CharField(max_length=30,default="")
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=100,default="positive")
    def __str__(self):
        return self.content
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    message = models.ForeignKey(Message)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text