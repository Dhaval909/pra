from django.db import models

# Create your models here.
class Todo(models.Model):
    todolist = models.CharField(max_length=200)