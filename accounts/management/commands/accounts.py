import json
import random
from datetime import timedelta, datetime, date

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from accounts.models import User, School, Company, JobTitle, Hometown, Location
from accounts.choices import Gender, MaritalStatus, Zodiac, Smoke, Religion, Politics, EducationLevel


def get_name_surname():
    with open('resources/account/name_surname_list') as f:
        lines = f.read().splitlines()
    return lines


def get_country():
    return random.choice(Location.objects.all())


def get_hometown():
    return random.choice(Hometown.objects.all())


def get_company():
    return random.choice(Company.objects.all())


def get_job_title():
    return random.choice(JobTitle.objects.all())


def get_college():
    return random.choice(School.objects.all())


def random_date():
    d1 = datetime.strptime('1963-01-01', '%Y-%m-%d')
    d2 = datetime.strptime('2004-01-01', '%Y-%m-%d')
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (d1 + timedelta(seconds=random_second)).date()


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_choice(choice):
    return random.choice([c[0] for c in choice.choices])


def generate_schools():
    universities = json.load(open('resources/account/universities.json'))
    for university in universities:
        school = School()
        school.name = university['name']
        school.country = university['country']
        school.save()


def generate_companies():
    companies = json.load(open('resources/account/companies.json'))
    for c in companies:
        company = Company()
        company.name = c['Name']
        company.sector = c['Sector']
        company.symbol = c['Symbol']
        company.save()


def generate_job_titles():
    job_titles = json.load(open('resources/account/job_title.json'))
    for j in job_titles:
        job_title = JobTitle()
        job_title.name = j
        job_title.save()


def generate_hometowns():
    hometowns = json.load(open('resources/account/countries_with_nationality.json'))
    for ht in hometowns:
        hometown = Hometown()
        hometown.country = ht['country']
        hometown.nationality = ht['nationality']
        hometown.save()


def generate_locations():
    cities = json.load(open('resources/account/cities.json'))
    for city in cities:
        location = Location()
        location.city = city['name']
        try:
            location.save()
        except IntegrityError as err:
            if 'duplicate' not in err.args[0]:
                raise err


def generate_accounts():
    for name_surname in get_name_surname():
        user = User()
        user.first_name = name_surname.split(' ')[0]
        user.last_name = name_surname.split(' ')[1]
        if User.objects.filter(username=user.first_name.lower() + user.last_name.lower()):
            user.username = user.first_name.lower() + user.last_name.lower() + str(random.randint(0, 100))
        else:
            user.username = user.first_name.lower() + user.last_name.lower()
        user.set_password(user.first_name)
        email_account = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'icloud.com'])
        user.email = user.first_name.lower() + user.last_name.lower() + '@' + email_account
        user.gender = get_choice(Gender)
        user.birth_date = random_date()
        user.age = calculate_age(user.birth_date)
        user.weight = random.randint(45, 120)
        user.height = random.randint(120, 220)
        user.marital_status = get_choice(MaritalStatus)
        user.nationality = get_hometown()
        user.hometown = user.nationality
        user.location = get_country()
        user.company = get_company()
        user.job_title = get_job_title()
        user.zodiac = get_choice(Zodiac)
        user.smoke = get_choice(Smoke)
        user.religion = get_choice(Religion)
        user.politics = get_choice(Politics)
        user.school = get_college()
        user.education_level = get_choice(EducationLevel)
        user.save()
        print('account created: id: {}, username: {}'.format(user.pk, user.username))


class Command(BaseCommand):

    def handle(self, *args, **options):
        generate_schools()
        generate_companies()
        generate_job_titles()
        generate_hometowns()
        generate_locations()
        generate_accounts()
