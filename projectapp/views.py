from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import VoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def project_list(request):
    projects = Project.objects.all().order_by('-score_sum', '-score_count')
    return render(request, 'projectapp/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            project.score_sum += score
            project.score_count += 1
            project.save()
            return HttpResponseRedirect(reverse('project_detail', args=[pk]))
        else:
            form = VoteForm()
    return render(request, 'projectapp/project_detail.html', {'project': project, 'form': form})