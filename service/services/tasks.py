from celery import shared_task
# from services.models import * 
from django.db.models import F
import time
from celery_singleton import Singleton
import datetime
from django.db import transaction



@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription

    #? Все действия выполняются вместе, атомарно
    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().filter(id=subscription_id).annotate(annotated_price=F('service__full_price') - F('service__full_price') * F('plan__discount_percent') / 100.00).first()

        subscription.price = subscription.annotated_price
        subscription.save()




@shared_task(base=Singleton)
def set_comment(subscription_id):
    from services.models import Subscription
    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)

        subscription.comment = str(datetime.datetime.now())
        subscription.save()

    