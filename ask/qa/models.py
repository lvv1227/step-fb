from django.db import models
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title=models.TextField(default='')
    text=models.TextField(default='')
    added_at=models.DateTimeField(default=timezone.now())
    rating=models.IntegerField(default=0)
    author=models.ForeignKey(User)
    def __str__(self):
        return self.title

class Answer(models.Model):
    text=models.TextField(default='')
    added_at=models.DateTimeField(default=timezone.now())
    question=models.ForeignKey(Question)
    author=models.ForeignKey(User)
    def __str__(self):
        return self.text