""" Models module """
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    """ Task db model """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Task ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title