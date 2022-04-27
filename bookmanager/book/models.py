from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10)

class People(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)