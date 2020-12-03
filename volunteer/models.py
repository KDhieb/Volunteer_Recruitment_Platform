from django.contrib.auth.models import User
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


class Entity(models.Model):
    name = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=15, blank=True, default="")
    email = models.CharField(max_length=50, blank=True, default="")
    address = models.CharField(max_length=200, blank=True, default="")
    about = models.TextField(blank=True, default='')
    access = models.IntegerField(default=-1)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class NPO(Entity):
    access = ACCESS['NPO']


class Listing(models.Model):
    title = models.CharField(max_length=200, unique=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey(NPO, on_delete=models.CASCADE, related_name='listings')
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


class Volunteer(Entity):
    access = ACCESS['Volunteer']
    photo = models.ImageField(blank=True, upload_to="images")
    registered = models.ManyToManyField(Listing, related_name="Registered", blank=True)
    favorites = models.ManyToManyField(Listing, related_name="Favorites", blank=True)
