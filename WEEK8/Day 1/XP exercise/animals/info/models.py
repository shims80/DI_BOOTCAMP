from django.db import models

# Create your models here.


class person(models.Model):
    name = models.CharField(max_length= 250)
    last_login = models.CharField(max_length=250)
