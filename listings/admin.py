from django.contrib import admin

from .models import Listing #this should be the same as models

admin.site.register(Listing)