from django.contrib import admin
from .models import * 


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_price']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan_type', 'discount_percent']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id']
