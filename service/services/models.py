from django.db import models
from django.core.validators import MaxValueValidator
from .tasks import * 
class Service(models.Model):

    name = models.CharField(("name"), max_length=50)
    full_price = models.PositiveIntegerField()


    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_price = self.full_price

    def save(self, *args, **kwargs):

        if self.full_price != self.__full_price:
            for sub in self.subscribtions.all():
                set_price.delay(sub.id)

        return super().save(*args, **kwargs)




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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):

        if self.discount_percent != self.__discount_percent:
            for sub in self.subscribtions.all():
                set_price.delay(sub.id)

        return super().save(*args, **kwargs)



class Subscription(models.Model):
    client = models.ForeignKey('clients.Client', related_name='subscribtions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscribtions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscribtions', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(default=0)
    comment = models.CharField(("comment"), max_length=50, default='')

