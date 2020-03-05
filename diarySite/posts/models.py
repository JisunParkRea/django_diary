import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title_text = models.CharField(max_length=100)
    content_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title_text
