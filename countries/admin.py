from django.contrib import admin
from .models import Country
# Register your models here.
@admin.register(Country)
class CoutnryAdmin(admin.ModelAdmin):
    pass

