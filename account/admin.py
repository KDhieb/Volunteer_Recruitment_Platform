from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import Group

from account.models import UserAccount

admin.site.register(UserAccount)

