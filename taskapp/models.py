from django.db import models
from django.contrib.auth.models import User


# class user, implement logic
# class User

class TaskTag(models.Model):
    name = models.CharField(max_length=255)


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    creator = models.ForeignKey(User, related_name="creator", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(User,related_name="assignee", on_delete=models.SET_NULL, null=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]