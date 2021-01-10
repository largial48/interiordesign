from django.contrib import admin
from .models import item,system,contact

# Models Registeration is done here
admin.site.register(item)
admin.site.register(system)
admin.site.register(contact)

# Django Admin SuperUser details = Name: shivam , Password: shivam
# check contacts table in it