from django.contrib import admin
from .models import Student, Subject, Marks

# Register your models here.
admin.site.register([Student, Subject, Marks])