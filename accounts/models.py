from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from accounts.choices import Religion, Gender, MaritalStatus, Zodiac, Smoke, Politics, EducationLevel


class School(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sector = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Hometown(models.Model):
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    # city = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.country


class Location(models.Model):
    # country = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.city


class User(AbstractUser):
    gender = models.CharField(max_length=30, blank=True, choices=Gender.choices)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=30, blank=True, choices=MaritalStatus.choices)
    nationality = models.ForeignKey(Hometown, models.CASCADE, blank=True, null=True,
                                    related_name='hometown_nationality')
    hometown = models.ForeignKey(Hometown, models.CASCADE, blank=True, null=True, related_name='hometown_city')
    location = models.ForeignKey(Location, models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, models.CASCADE, blank=True, null=True)
    job_title = models.ForeignKey(JobTitle, models.CASCADE, blank=True, null=True)
    zodiac = models.CharField(max_length=30, blank=True, choices=Zodiac.choices)
    smoke = models.CharField(max_length=30, blank=True, choices=Smoke.choices)
    bio = models.TextField(max_length=500, blank=True)
    religion = models.CharField(max_length=30, blank=True, choices=Religion.choices)
    politics = models.CharField(max_length=30, blank=True, choices=Politics.choices)
    school = models.ForeignKey(School, models.CASCADE, blank=True, null=True)
    education_level = models.CharField(max_length=30, blank=True, choices=EducationLevel.choices)
