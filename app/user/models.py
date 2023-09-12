from django.db import models

# Create your models here.
class Demo(models.Model):
    image = models.ImageField(upload_to='users/',)
    file = models.FileField(upload_to='userfile/',null=True,blank=True)


class ExcelDemo(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    number = models.IntegerField(null=False,blank=False)
    country_code = models.CharField(max_length=200,default='91')
    description = models.TextField(null=False,blank=False)


    def save(self,*args,**kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

