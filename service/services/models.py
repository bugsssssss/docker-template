from django.db import models
from django.core.validators import MaxValueValidator

class Service(models.Model):

    name = models.CharField(("name"), max_length=50)
    full_price = models.PositiveIntegerField()


    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name


class Plan(models.Model): 
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )

    plan_type = models.CharField(("plan types"), max_length=20, choices=PLAN_TYPES)
    discount_percent = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(100)
    ])


class Subscription(models.Model):
    client = models.ForeignKey('clients.Client', related_name='subscribtions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscribtions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscribtions', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(default=0)


