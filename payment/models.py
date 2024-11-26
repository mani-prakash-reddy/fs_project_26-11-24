# payment/models.py
from django.db import models

class WebvisitorCard(models.Model):
    card_id = models.CharField(max_length=10, primary_key=True)
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=100)
    cvv = models.CharField(max_length=4)
    expiry = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card_name} - {self.card_id}"