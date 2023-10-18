from django.db import models

# Create your models here.
class FormModel(models.Model):    
    name = models.CharField(max_length=100,blank=True , null=True)
    mobile = models.CharField(max_length=100,blank=True , null=True)
    mail = models.CharField(max_length=100 , blank=True , null=True)
    city = models.CharField(max_length=100 , blank=True , null=True)
    counts = models.CharField(max_length=100 , blank=True , null=True)
    def __str__(self):
        return self.name