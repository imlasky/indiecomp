from indiecomp.jobs.models import Job, Company, Location

from celery import shared_task

@shared_task
def add(x,y):
    return x + y