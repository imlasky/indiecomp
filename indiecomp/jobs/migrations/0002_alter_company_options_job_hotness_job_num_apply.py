# Generated by Django 4.1.5 on 2023-01-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name": "Company", "verbose_name_plural": "Companies"},
        ),
        migrations.AddField(
            model_name="job",
            name="hotness",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="job",
            name="num_apply",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
