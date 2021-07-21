# import django
from django.contrib import admin

# import models
from .models import Project

# register 
admin.site.register(Project)
