from django.db import models

# Create your models here.
class Demo(models.Model):
    image = models.ImageField(upload_to='users/',)