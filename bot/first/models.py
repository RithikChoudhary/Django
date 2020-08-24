from django.db import models

# Create your models here.
class medicine(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    quantity = models.IntegerField()
    desc = models.TextField()
    comp = models.CharField(max_length=200)
     