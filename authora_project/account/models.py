from django.db import models
from django.utils import timezone
from datetime import timedelta

class UserRegistration(models.Model):
    username=models.CharField(max_length=150,unique=True,)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=128)
    roles=models.CharField(max_length=10)

    last_activity = models.DateTimeField(null=True, blank=True)

    def is_online(self):
        if self.last_activity:
            return self.last_activity >= timezone.now() - timedelta(minutes=5)
        return False
    

    def __str__(self):
        return self.username



