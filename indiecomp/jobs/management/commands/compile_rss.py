import feedparser
from ._indeed_parser import parse_entry
from django.core.management.base import BaseCommand, CommandError
from indiecomp.jobs.models import Job, Company, Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        news_feed = feedparser.parse("https://rss.indeed.com/rss?q=backend+engineer&sort=date")

        for entry in news_feed.entries:
            res = parse_entry(entry)
            company, created = Company.objects.get_or_create(name=res["company"])
            if created:
                company.save()
            
