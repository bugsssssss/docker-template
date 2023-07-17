from django.contrib import admin
from .models import * 

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'full_address']
