from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.

ACCESS = {'NPO': 0, 'Volunteer': 1}

ONCE = "One-time"
WEEKLY = "Weekly"
MONTHLY = "Monthly"

CHOICES = [
    (ONCE, "Once"),
    (WEEKLY, "Weekly"),
    (MONTHLY, "Monthly"),
]

# class Entity(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     number = models.CharField(max_length=15, blank=True, default="")
#     email = models.CharField(max_length=50, blank=True, default="")
#     address = models.CharField(max_length=200, blank=True, default="")
#     about = models.TextField(blank=True, default='')
#     access = models.IntegerField(default=-1)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return str(self.name)


class User(AbstractUser):
    is_volunteer = models.BooleanField('volunteer status', default=False)
    is_npo = models.BooleanField('npo status', default=False)
    email = models.CharField(max_length=50, blank=True, default="")
    number = models.CharField(max_length=15, blank=True, default="")
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True, default="")
    about = models.TextField(blank=True, default='')


class NPO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user.name)

class Listing(models.Model):
    title = models.CharField(max_length=200, unique=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey('NPO', on_delete=models.CASCADE)
    commitment = models.CharField(max_length=32, choices=CHOICES, default=WEEKLY)
    city = models.CharField(max_length=30, default="")
    text = RichTextField(blank=True, default="")
    requirements = RichTextField(blank=True, default="")

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"
        ordering = ['-pub_date']

    def __str__(self):
        return str(self.title) + ": " + str(self.org)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    registered = models.ManyToManyField(Listing, related_name="Registered", blank=True)
    favorites = models.ManyToManyField(Listing, related_name="Favorites", blank=True)

    def __str__(self):
        return str(self.user.name)

