# Generated by Django 3.1.1 on 2021-01-02 05:12

import ckeditor.fields
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_volunteer', models.BooleanField(default=False, verbose_name='volunteer status')),
                ('is_npo', models.BooleanField(default=False, verbose_name='npo status')),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('number', models.CharField(blank=True, default='', max_length=15)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('about', models.TextField(blank=True, default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('commitment', models.CharField(choices=[('One-time', 'Once'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='Weekly', max_length=32)),
                ('city', models.CharField(default='', max_length=30)),
                ('text', ckeditor.fields.RichTextField(blank=True, default='')),
                ('requirements', ckeditor.fields.RichTextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='NPO',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='volunteer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='volunteer.user')),
                ('favorites', models.ManyToManyField(blank=True, related_name='Favorites', to='volunteer.Listing')),
                ('registered', models.ManyToManyField(blank=True, related_name='Registered', to='volunteer.Listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.npo'),
        ),
    ]