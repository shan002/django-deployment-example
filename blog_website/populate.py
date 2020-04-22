import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_website.settings')

import django
django.setup()

from django.contrib.auth.models import User
from blog_app.models import Newpost
from django.utils import timezone
from faker import Faker
import random


def populate_user(N=5):
    fake = Faker()
    for _ in range(N):
        fake_username = fake.name()
        fake_email = fake.email()
        fake_password = fake.password()

        User.objects.get_or_create(username=fake_username, email=fake_email, password=fake_password)


def populate_post(N=5):
    fake = Faker()
    for _ in range(N):
        random_author = random.choice(User.objects.all())
        fake_post_name = fake.city()
        fake_post = fake.text(max_nb_chars=random.randint(1000, 3000))
        fake_published_date = fake.date_time(tzinfo=timezone.get_current_timezone())

        Newpost.objects.get_or_create(author=random_author, post_name=fake_post_name, post=fake_post, published_date=fake_published_date)


if __name__ == '__main__':
    choice = int(input("Option 1: Populate User\n"
                       "Option 2: Populate Post\n"
                       "Choose between 1 or 2 : "))
    if choice == 1:
        print("Populate User")
        num = int(input("How many users do you wanna create? "))
        print("Populating users...")
        populate_user(num)
        print("Populating users complete!")

    elif choice == 2:
        print("Populate Post")
        num = int(input("How many posts do you wanna create? "))
        print("Populating posts...")
        populate_post(num)
        print("Populating posts complete!")
