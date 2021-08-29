from django.contrib import admin
from .models import staff
from .models import attendance
# Register your models here.

admin.site.register(staff)
admin.site.register(attendance)