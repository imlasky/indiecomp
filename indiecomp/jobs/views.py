from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView

from indiecomp.jobs.models import Job

User = get_user_model()


class JobListView(ListView):
    model = Job
    # paginate_by = 100
    queryset = Job.objects.all().filter(approved=Job.APPROVED)
    # [o.save() for o in queryset.all()]
    ordering = ["-hotness"]
    context_object_name = "job_list"
    template_name = "pages/home.html"


def apply(request, pk):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=pk)
        job.num_apply += 1
        job.save()
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            user.saved_jobs.add(job)
            user.save()
        return redirect(job.application_url)
    return redirect("/")


def remove_job_from_user(request, pk):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=pk)
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            user.saved_jobs.remove(job)
            user.save()
        return redirect(f"/users/{user.username}")
    return redirect("/")


def post_review_job_posting(request, pk):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=pk)
        if request.user.is_superuser:
            job.approved = request.POST["decision"]
            job.save()
        else:
            return redirect("/")
        return redirect("/jobs/review/")
    return redirect("/")


class JobReviewList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Job
    queryset = Job.objects.all().filter(approved=Job.PENDING)
    template_name = "jobs/job_review.html"
