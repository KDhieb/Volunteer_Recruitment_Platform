from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

from django.contrib.auth.models import User, AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from volunteer.models import NPO, Volunteer, ACCESS

# class User(AbstractUser):
#     is_volunteer = models.BooleanField('volunteer status', default=False)
#     is_npo = models.BooleanField('npo status', default=False)
#
#     #email = models.CharField(max_length=50, blank=True, default="")
#     name = models.CharField(max_length=100, blank=True)
#     number = models.CharField(max_length=15, blank=True, default="")
#     address = models.CharField(max_length=200, blank=True, default="")
#     about = models.TextField(blank=True, default='')






#
# class UserAccount(User, models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
#     object_id = models.PositiveIntegerField(null=True)
#     user_gfk = GenericForeignKey('content_type', 'object_id')
#     access = models.IntegerField(default=-1)
#
#     def __init__(self, access_type=-1, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if access_type == ACCESS['NPO']:
#             self.user_gfk = NPO()
#             self.access = ACCESS['NPO']
#
#         elif access_type == ACCESS['Volunteer']:
#             self.user_gfk = Volunteer()
#             self.access = ACCESS['Volunteer']
#
#     def __str__(self):
#         return self.username
#
#     def isNPO(self):
#         return self.user_gfk.access == ACCESS['NPO']
#
#     def isVolunteer(self):
#         return self.user_gfk.access == ACCESS['Volunteer']
