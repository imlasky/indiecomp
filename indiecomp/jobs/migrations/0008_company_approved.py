# Generated by Django 4.1.5 on 2023-01-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0007_alter_company_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="approved",
            field=models.CharField(
                choices=[("A", "Approved"), ("P", "Pending"), ("R", "Rejected")],
                default="P",
                max_length=1,
            ),
        ),
    ]