from django.shortcuts import render
from django.views.generic.list import ListView

from indiecomp.jobs.models import Job

class JobListView(ListView):
    model = Job
    paginate_by = 100
    context_object_name = "job_list"
    template_name = "pages/home.html"