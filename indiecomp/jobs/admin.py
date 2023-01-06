from django.contrib import admin
from .models import Job, Location, Company

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "salaryMin", "salaryMax"]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city", "country"]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
