from datetime import datetime

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
        return self.tasks.filter(status=Task.TODO).count()


class Task(models.Model):
    #
    # Status choices

    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    )

    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=TODO)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def registered_time(self):
        return 0

class Entry(models.Model):
    project = models.ForeignKey(Project, related_name='entries', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='entries', on_delete=models.CASCADE)
    minutes = models.IntegerField(default=0)
    is_tracked = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True,default=datetime.today())

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.task:
            return '%s - %s' % (self.task.title, self.created_at)

        return '%' % self.created_at 