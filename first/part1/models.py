from django.db import models

# Create your models here.

class Objects(models.Model):
    data = models.CharField(max_length=200,blank=False)

