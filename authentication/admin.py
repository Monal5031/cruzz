# Django
from django.contrib import admin
# local Django
from authentication.models import User


admin.site.register(User)
