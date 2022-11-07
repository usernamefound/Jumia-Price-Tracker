from django.contrib import admin
from .models import Link, CustomUser

admin.site.register(CustomUser)
admin.site.register(Link)
