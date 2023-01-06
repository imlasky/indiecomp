from django.urls import path

from indiecomp.jobs.views import JobListView

app_name = "jobs"
urlpatterns = [
    path("", view=JobListView.as_view(), name="job_list"),
    # path("/jobs/[")
]
