from django.contrib import admin

from .models import Company, Job, Location


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "salary_min", "salary_max"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city", "country"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
