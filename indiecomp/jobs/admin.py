from django.contrib import admin

from .models import Company, Feed, Job, Location


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "salary_min", "salary_max", "company"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city", "country"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ["source_name", "search_term", "url"]
