# Generated by Django 2.2.12 on 2020-04-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='new_field',
        ),
    ]
