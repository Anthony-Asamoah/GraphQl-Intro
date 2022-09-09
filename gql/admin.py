from django.contrib import admin
from . import models


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Chef)
class ChefAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass
