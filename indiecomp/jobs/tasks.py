import logging

import feedparser
from celery import shared_task

from indiecomp.jobs.helpers._indeed_parser import parse_entry
from indiecomp.jobs.models import Company, Feed, Job, Location

logger = logging.Logger(__name__)


@shared_task
def update_rss():

    for feed in Feed.objects.filter(active=True):
        news_feed = feedparser.parse(feed.url)

        for entry in news_feed.entries:

            res = parse_entry(entry)
            company, created = Company.objects.get_or_create(name=res["company"])
            if created:
                company.save()
            location, created = Location.objects.get_or_create(city=res["city"])

            if created:
                location.save()

            job = Job.objects.get(
                title=res["title"],
                company=company,
                location=location,
                application_url=res["application_url"],
            )
            if not job:
                new_job = Job.objects.create(
                    title=res["title"],
                    salary_min=res["salary_min"],
                    salary_max=res["salary_max"],
                    company=company,
                    application_url=res["application_url"],
                    description=res["description"],
                    from_automation=True,
                    approved=company.approved,
                )
                new_job.location.add(location)
                job.save()
