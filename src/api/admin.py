from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Seru)
class SeruAdmin(admin.ModelAdmin):
    pass
