from django.contrib import admin

from volunteer.models import NPO, Volunteer, Listing 

# Register your models here.

admin.site.register(NPO)
admin.site.register(Volunteer)
admin.site.register(Listing)
