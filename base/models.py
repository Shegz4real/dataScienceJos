from django.db import models
from django.utils import timezone

# C./ma reate your models here.

class ComMember(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length = 20, null = False)
    surname = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 14, null = False)
    message = models.TextField()
    
    def __str__(self):
        return self.email