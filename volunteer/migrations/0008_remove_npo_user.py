# Generated by Django 3.1.1 on 2020-11-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0007_npo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npo',
            name='user',
        ),
    ]