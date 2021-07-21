from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Import models
from django.contrib.auth.models import User
from .models import Project

# View

@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project = Project.objects.create( title=title, created_by=request.user)

            return redirect('project:projects')

    return render(request, 'project/projects.html', {'projects' : projects})