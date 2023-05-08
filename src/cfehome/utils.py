from faker import Faker
from pprint import pprint
import csv
from django.conf import settings

MOVIE_METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def load_movie_data(limit=2):
    with open(MOVIE_METADATA_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            pprint(row)
            if i+1>limit:
                break

def get_fake_profiles(count=10):
    fake = Faker()
    user_data = []
    for _ in range(count):
        profile = fake.profile()
        data = {
            "username": profile.get('username'),
            "email": profile.get("mail"),
            # "password": make_password(fake.password(length=15)),
            "is_active": True,
        }
        if 'name' in profile:
            fname, lname = profile.get('name').split(" ")[:2]
            data['first_name'] = fname
            data['last_name'] = lname
        user_data.append(data)
        # print(fake.profile())
    return user_data