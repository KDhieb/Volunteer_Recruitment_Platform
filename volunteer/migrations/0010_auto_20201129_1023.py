# Generated by Django 3.1.1 on 2020-11-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0009_auto_20201128_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npo',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]