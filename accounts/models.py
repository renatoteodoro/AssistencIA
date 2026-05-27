from django.conf import settings
from django.db import models


class Account(models.Model):
    CHECKING = 'checking'
    SAVINGS = 'savings'
    WALLET = 'wallet'
    ACCOUNT_TYPE_CHOICES = [
        (CHECKING, 'Corrente'),
        (SAVINGS, 'Poupança'),
        (WALLET, 'Carteira'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    name = models.CharField(max_length=100)
    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPE_CHOICES,
    )
    initial_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
