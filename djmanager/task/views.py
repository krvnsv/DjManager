from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from project.models import Project
from todolist.models import Todolist
from .models import Task


@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        Task.objects.create(project=project, todolist=todolist, name=name, description=description, created_by=request.user)
    
        return redirect(f'/projects/{project_id}/{todolist_id}/')
    return render(request, 'task/add.html')