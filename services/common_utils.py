import os
from decimal import Decimal, ROUND_UP

from services.enums import Profile


def get_id_from_db(clazz, **kwargs):
    return clazz.objects.get(**kwargs).id


def get_profile():
    profile = os.getenv('PROFILE')
    if profile:
        return Profile(profile)
    else:
        return Profile.DEV


def remove_duplicates(l):
    return list(dict.fromkeys(l))


def flatten_list(l):
    return [item for sublist in l for item in sublist]
