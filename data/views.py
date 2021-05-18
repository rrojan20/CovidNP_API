from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Last24Hours, Total
from scraper import scrape
from datetime import date


def scrape_view(request):
    """
    Scrape but store only one database entry per day.
    
    If multiple scrapings are done in one day, remove all previous db entries for the day
    before creating the new object
    """

    url = "https://covid19.mohp.gov.np/"

    today_data, total_data = scrape(url)

    old_objects = Last24Hours.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    Last24Hours.objects.create(
        new_cases=today_data["New Cases"],
        recovered=today_data["Recovered"],
        deaths=today_data["Deaths"],
    )

    old_objects = Total.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    Total.objects.create(
        total_cases=total_data["Total Cases"],
        total_infected=total_data["Total Infected"],
        recovered=total_data["Recovered"],
        deaths=total_data["Deaths"],
    )

    return HttpResponse("Successfully scraped that shit")
