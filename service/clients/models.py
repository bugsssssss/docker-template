from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):

    user = models.OneToOneField(User, verbose_name=("Client"), on_delete=models.PROTECT)
    company_name = models.CharField(("company name"), max_length=100)
    full_address = models.CharField(("address"), max_length=100)

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.company_name


