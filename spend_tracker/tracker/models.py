from django.db import models
from django.contrib.auth.models import User  # For linking to Django's built-in User model


class BankAccount(models.Model):
    """
    Represents a user's bank account.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_accounts')
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"


class Transaction(models.Model):
    """
    Represents a transaction for a bank account.
    """
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True, null=True)  # Optional: Categorize transactions

    def __str__(self):
        return f"{self.date}: {self.description} - ${self.amount}"
