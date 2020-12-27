from django.contrib import admin

from volunteer.models import NPO, Volunteer, Listing, User

# Register your models here.

admin.site.register(User)
admin.site.register(NPO)
admin.site.register(Volunteer)
admin.site.register(Listing)
