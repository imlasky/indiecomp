import feedparser
from ._indeed_parser import parse_entry
from django.core.management.base import BaseCommand, CommandError
from indiecomp.jobs.models import Job, Company, Location
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        news_feed = feedparser.parse("https://rss.indeed.com/rss?q=tech&sort=date")

        for entry in news_feed.entries:
            
            res = parse_entry(entry)
            company, created = Company.objects.get_or_create(name=res["company"])
            if created:
                company.save()
            location, created = Location.objects.get_or_create(city=res["city"])

            if created:
                location.save()

            job, created = Job.objects.get_or_create(
                title=res["title"],
                salary_min=res["salary_min"],
                salary_max=res["salary_max"],
                company=company,
                application_url=res["application_url"],
                description=res["description"],
                from_automation=True,
                approved=company.approved,
            )

            if created:
                job.location.add(location)
                job.save()
            
