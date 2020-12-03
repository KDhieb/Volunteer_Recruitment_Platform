# Generated by Django 3.1.1 on 2020-09-29 16:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(blank=True, default='', max_length=15)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('about', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(blank=True, default='', max_length=15)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('about', models.TextField(blank=True, default='')),
                ('photo', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('requirements', ckeditor.fields.RichTextField(blank=True, default='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, default='')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='volunteer.npo')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
                'ordering': ['-pub_date'],
            },
        ),
    ]