# Generated by Django 3.2.23 on 2024-02-01 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customerdetails_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerDetails',
        ),
    ]