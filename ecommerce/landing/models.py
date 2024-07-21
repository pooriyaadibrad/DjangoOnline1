from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
# Create your models here.
class message(models.Model):
    FullName=models.CharField(max_length=100)
    Email=models.EmailField()
    phone_number=models.CharField(max_length=11,validators=[MaxLengthValidator(11),MinLengthValidator(11)])
    message=models.TextField(max_length=1000)
    def __str__(self):
        return self.FullName