# Generated by Django 4.1.5 on 2023-01-11 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0008_company_approved"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="salaryMax",
            new_name="salary_max",
        ),
        migrations.RenameField(
            model_name="job",
            old_name="salaryMin",
            new_name="salary_min",
        ),
    ]
