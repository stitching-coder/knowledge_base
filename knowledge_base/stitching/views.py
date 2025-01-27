from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'stitching/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'stitching/project_detail.html', {'project': project})
