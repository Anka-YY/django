from django.db import models
from datetime import datetime


class Registration(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=100)


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateTimeField(default=datetime.now().strftime("%d-%m-%Y %X"))
    due_date = models.DateTimeField(default=datetime.now().strftime("%d-%m-%Y %X"))
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)

    class Meta:
        ordering = ["-created"]


