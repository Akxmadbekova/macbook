from django.contrib import admin

# Register your models here.

from .models import MAC, iphone

admin.site.register(MAC)
admin.site.register(iphone)