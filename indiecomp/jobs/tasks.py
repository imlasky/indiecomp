from celery import shared_task

# from indiecomp.jobs.models import Company, Job, Location


@shared_task
def add(x, y):
    return x + y
