from django.db import models
from django.shortcuts import render
from django.http import HttpResponse

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'