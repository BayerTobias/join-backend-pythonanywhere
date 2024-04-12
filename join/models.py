from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    initials = models.CharField(max_length=5)
    color = models.CharField(max_length=10)


class Contact(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="contacts"
    )
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    initials = models.CharField(max_length=5)
    color = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


class Subtask(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, default="todo")
    priority = models.CharField(max_length=20, default="low")
    assigned_users = models.ManyToManyField(CustomUser, related_name="assigned_tasks")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None)

    subtasks = models.JSONField(default=list)
