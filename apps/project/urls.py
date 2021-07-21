from django.urls import path
from .views import projects

# URL patterns

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),

]