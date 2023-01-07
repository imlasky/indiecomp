from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView

from indiecomp.jobs.models import Job


class JobListView(ListView):
    model = Job
    paginate_by = 100
    context_object_name = "job_list"
    template_name = "pages/home.html"


def apply(request, pk):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=pk)
        job.num_apply += 1
        job.save()
        return redirect(job.application_url)
    return redirect("/")
