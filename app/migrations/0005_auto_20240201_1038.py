# Generated by Django 3.2.23 on 2024-02-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='hemoglobin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='pcv',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='platelet_count',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='rbc_count',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='rdw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]