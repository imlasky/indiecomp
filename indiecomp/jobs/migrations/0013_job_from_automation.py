# Generated by Django 4.1.5 on 2023-01-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0012_alter_job_salary_max_alter_job_salary_min"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="from_automation",
            field=models.BooleanField(default=False),
        ),
    ]
