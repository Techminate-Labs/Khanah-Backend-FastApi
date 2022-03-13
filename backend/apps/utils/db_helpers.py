import random

from slugify import slugify


def get_slug(title):
    return f"{slugify(title)}-{random.randint(100000, 999999)}"
