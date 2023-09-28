from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class Booking(models.Model):
   name=models.CharField(max_length=50) 
   email = models.EmailField(max_length=100,unique=True,validators=[EmailValidator()])
   dateTime = models.DateTimeField( auto_now_add=True,verbose_name="Date Created")
   peoples=models.IntegerField()
   specialrequest=models.TextField()
