from django.contrib.auth.models import User
from django.db import models

#
# Models

class Project(models.Model):
    title = models.CharField(max_length = 255)

    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def _str_(self):
        return self.title

    def registered_time(self):
        return 0

    def num_tasks_todo(self):
        return 0