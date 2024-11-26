# contactus/models.py
from django.db import models

class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Contact Us"