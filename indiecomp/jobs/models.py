import math
from datetime import datetime
from uuid import uuid4

from django.db import models


class Job(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(blank=False, null=False, max_length=250)
    salaryMin = models.PositiveIntegerField(blank=True)
    salaryMax = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=False)
    application_url = models.URLField(blank=False)

    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    location = models.ManyToManyField("Location")

    num_apply = models.PositiveIntegerField(default=0)
    hotness = models.FloatField(default=0)

    def set_hotness_score(self):
        order = math.log10(max(self.num_apply, 1))
        seconds = datetime.now().timestamp() - 1673063024
        hours = 12
        self.hotness = round(order + seconds / (hours * 3600), 15)
        # return hotness

    def save(self, *args, **kwargs):
        self.set_hotness_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Location(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Company(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
