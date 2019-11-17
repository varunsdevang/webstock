from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import sys
from django.utils import timezone


# Create your models here.


class User(models.Model):
    user_Name = models.CharField(max_length=150, unique=True)
    user_DOB = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    user_Email = models.EmailField()
    user_Password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_Name


class Portfolio(models.Model):
    user_Portfolio = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    port_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.port_Name


class Investment(models.Model):
    investment_parent = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(sys.maxsize)])
    investment_date = models.DateField()
    investment_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.investment_name


class Stock(Investment):
    investment_name = "Stock"
    stock_CODE = models.CharField(max_length=5)
    expected_Return_Rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])


class MutualFunds(Investment):
    investment_name = "MutualFunds"
    fund_Name = models.CharField(max_length=50)
    fund_Provider_Bank = models.CharField(max_length=50)
    return_Rate = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(5)])


class HedgeFunds(Investment):
    investment_name = "HedgeFunds"
    fund_Name = models.CharField(max_length=50)
    fund_Provider = models.CharField(max_length=50)
    return_Rate = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(5)])


class Cash(Investment):
    investment_name = "Cash"
    pass


class Bonds(Investment):
    investment_name = "Bonds"
    bond_Issuer = models.CharField(max_length=50)
    bond_Interest_Rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    bond_maturity_date = models.DateField()
