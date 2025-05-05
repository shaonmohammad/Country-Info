from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=10, unique=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    timezones = models.JSONField()
    flag_url = models.URLField(null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
