from tkinter import N
from django.db import models
from datetime import date


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.URLField()

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=40)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(default=date.today())
    date_completion = models.DateField()
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
