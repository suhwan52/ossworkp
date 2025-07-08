from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projectapp/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projectapp/project_detail.html', {'project': project})