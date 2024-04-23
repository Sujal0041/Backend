from django.db import models

# Create your models here.
from django.db import models
from sujal.models import CustomUser
from finance.models import Wallet
from category.models import Category

# Create your models here.
class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)