# Generated by Django 4.1.5 on 2023-01-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_company_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(),
        ),
    ]