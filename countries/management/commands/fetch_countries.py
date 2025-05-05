import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = "Fetch and store countries from external API"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        data = response.json()

        for item in data:
            Country.objects.update_or_create(
                cca2=item.get("cca2"),
                defaults={
                    "name": item.get("name", {}).get("common"),
                    "capital": item.get("capital", [None])[0],
                    "population": item.get("population"),
                    "region": item.get("region"),
                    "timezones": item.get("timezones", []),
                    "flag_url": item.get("flags", {}).get("png"),
                    "languages": item.get("languages", {}),
                },
            )
        self.stdout.write(self.style.SUCCESS("Countries fetched and stored."))
