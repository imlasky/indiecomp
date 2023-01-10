from django.urls import path

from indiecomp.jobs.views import (
    JobCreateView,
    JobListView,
    JobReviewList,
    apply,
    post_review_job_posting,
    remove_job_from_user,
)

app_name = "jobs"
urlpatterns = [
    path("", view=JobListView.as_view(), name="job_list"),
    path("jobs/create/", view=JobCreateView.as_view(), name="create"),
    path("jobs/review/", view=JobReviewList.as_view(), name="review"),
    path(
        "jobs/<uuid:pk>/review/",
        view=post_review_job_posting,
        name="post_review_job_posting",
    ),
    path("jobs/<uuid:pk>/apply/", view=apply, name="apply"),
    path(
        "jobs/<uuid:pk>/remove_from_user/",
        view=remove_job_from_user,
        name="remove_job_from_user",
    ),
]
