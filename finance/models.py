from django.db import models
from sujal.models import CustomUser


class Wallet(models.Model):
    # WALLET_TYPES = (
    #     ('checking', 'Checking'),
    #     ('savings', 'Savings'),
    #     ('credit_card', 'Credit Card'),
    #     ('cash', 'Cash'),
    #     ('investment', 'Investment'),
    #     ('other', 'Other'),
    # )
    
    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=20, choices=WALLET_TYPES)
    type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class FinanceTransaction(models.Model):
    # TRANSACTION_TYPES = (
    #     ('income', 'Income'),
    #     ('expense', 'Expense'),
    # )
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    type = models.CharField(max_length=10)
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    category = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.type} - {self.category}"


