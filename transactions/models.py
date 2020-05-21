from django.db import models
from musers.models import Muser


class Transaction(models.Model):
    user = models.ForeignKey(Muser, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    deposit = models.IntegerField()
    withdrawal = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)[:50]

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
