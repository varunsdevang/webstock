from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class User(models.Model):
    user_Name = models.CharField(max_length=150)
    user_DOB = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    user_Email=models.EmailField()
    user_Password=models.CharField(max_length=20)

    def __str__(self):
        return self.user_Name

