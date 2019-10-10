from django.contrib import admin
from .models import Person, Passport

admin.site.register(Passport)
admin.site.register(Person)
