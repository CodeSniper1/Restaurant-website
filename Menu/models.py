from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class Menu(models.Model):
   name=models.CharField(max_length=50) 
   description=models.TextField()
   price=models.IntegerField()
   image=models.FileField(upload_to="Menu/",max_length=250,null=True,default=None)
   availabilityTime=models.CharField(max_length=50,default="N/A")