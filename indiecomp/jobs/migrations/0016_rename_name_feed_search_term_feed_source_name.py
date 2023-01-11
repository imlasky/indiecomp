# Generated by Django 4.1.5 on 2023-01-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0015_feed_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feed",
            old_name="name",
            new_name="search_term",
        ),
        migrations.AddField(
            model_name="feed",
            name="source_name",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]