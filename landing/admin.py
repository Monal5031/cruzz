# Django
from django.contrib import admin

# local Django
from landing.models import CustomUser


admin.site.register(CustomUser)
