from django.db import models
import datetime

# Create your models here.
class task(models.Model):
    task=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True, blank=True)