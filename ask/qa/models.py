from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    title=models.TextField
    text=models.TextField
    added_at=
