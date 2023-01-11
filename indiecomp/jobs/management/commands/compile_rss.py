import feedparser
from ._indeed_parser import parse_entry
from django.core.management.base import BaseCommand, CommandError
from indiecomp.jobs.models import Job, Company, Location
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        news_feed = feedparser.parse("https://rss.indeed.com/rss?q=backend+engineer&sort=date")
        

        # print(news_feed.entries[0]["link"].split("&from=rss")[0])
        # print(news_feed.entries[0]['summary'])
        # for entry in news_feed.entries:
            
        #     res = parse_entry(entry)
        #     print(res)
        #     company, created = Company.objects.get_or_create(name=res["company"])
        #     if created:
        #         company.save()
            # job, created = Job.objects.get_or_create(
            #     title=res["title"],
            #     salaryMin=res["salaryMin"],
            #     salaryMax=res["salaryMax"],
            #     company=company,
            # )
            
