from django.db import models
import datetime
import uuid
from django.contrib.auth import get_user_model


User = get_user_model()




class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(blank=True, max_length=100)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-created']


    def __str__(self):
        return self.title
