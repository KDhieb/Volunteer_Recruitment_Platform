from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from volunteer.models import NPO, Volunteer, Entity, ACCESS


class UserAccount(User, models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    user_gfk = GenericForeignKey('content_type', 'object_id')

    def __init__(self, access_type=-1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if access_type == ACCESS['NPO']:
            self.user_gfk = NPO()
        elif access_type == ACCESS['Volunteer']:
            self.user_gfk = Volunteer()

    def __str__(self):
        return self.id
