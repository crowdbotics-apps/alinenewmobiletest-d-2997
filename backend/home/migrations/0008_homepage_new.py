# Generated by Django 2.2.12 on 2020-04-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_remove_homepage_another_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="new",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
