import math
from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models

# class JobManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset()


class Job(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    APPROVED = "A"
    PENDING = "P"
    REJECTED = "R"
    APPROVAL_CHOICES = [
        (APPROVED, "Approved"),
        (PENDING, "Pending"),
        (REJECTED, "Rejected"),
    ]
    approved = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default=PENDING)

    title = models.CharField(blank=False, null=False, max_length=250)
    salary_min = models.FloatField(
        blank=True, null=True, validators=[MinValueValidator(0.0)]
    )
    salary_max = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=False)
    application_url = models.URLField(blank=False)
    from_automation = models.BooleanField(default=False)

    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    location = models.ManyToManyField("Location")

    num_apply = models.PositiveIntegerField(default=0)
    hotness = models.FloatField(default=0)

    def get_hotness_score(self):
        order = math.log10(max(self.num_apply, 1))
        seconds = self.created_at.timestamp() - 1673063024
        hours = 12.5
        return round(order + seconds / (hours * 3600), 15)

    def save(self, *args, **kwargs):
        if self.created_at:
            self.hotness = self.get_hotness_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Location(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Company(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    APPROVED = "A"
    PENDING = "P"
    REJECTED = "R"
    APPROVAL_CHOICES = [
        (APPROVED, "Approved"),
        (PENDING, "Pending"),
        (REJECTED, "Rejected"),
    ]
    approved = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default=PENDING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Feed(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    source_name = models.CharField(max_length=100)
    search_term = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=False)
