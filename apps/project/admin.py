# import django
from django.contrib import admin

# import models
from .models import Project, Task

# register 
admin.site.register(Project)
admin.site.register(Task)