from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class Chef(models.Model):
   name=models.CharField(max_length=50) 
   designation=models.TextField()
   image=models.FileField(upload_to="Chef/",max_length=250,null=True,default=None)