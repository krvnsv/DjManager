from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Project

@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project/projects.html',{
        'projects': projects
    })