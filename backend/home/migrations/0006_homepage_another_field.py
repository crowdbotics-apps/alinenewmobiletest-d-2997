# Generated by Django 2.2.12 on 2020-04-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_remove_homepage_new_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="another_field",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
