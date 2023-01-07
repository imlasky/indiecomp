from django.urls import path

from indiecomp.jobs.views import JobListView, apply, remove_job_from_user

app_name = "jobs"
urlpatterns = [
    path("", view=JobListView.as_view(), name="job_list"),
    path("jobs/<uuid:pk>/apply/", view=apply, name="apply"),
    path("jobs/<uuid:pk>/remove_from_user/", view=remove_job_from_user, name="remove_job_from_user")
]
