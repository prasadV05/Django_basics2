from django.db import models

# Create your models here.
class My_app(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)