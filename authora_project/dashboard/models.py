from django.utils import timezone
from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(null=True, blank=True)

    def is_online(self):
        if self.last_activity:
            return self.last_activity >= timezone.now() - timedelta(minutes=5)
        return False

    def __str__(self):
        return self.username