# Generated by Django 2.2.12 on 2020-04-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200415_2141"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="new_field",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
