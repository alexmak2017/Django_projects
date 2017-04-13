from django.core.management.base import BaseCommand
from accounts.models import User

from publications.models import Publication
from random import randint, choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(User.objects.all())
        print(self.get_version())
        print(self.check_migrations())

        for index in range(1000):
            users = User.objects.values_list("id", flat=True)
            rand_user = choice(users)
            Publication.objects.create(title="Title",
                                       body="some text"*randint(50,100),
                                       image="publications/58c3c109-2efa-4dfa-8ddc-106cf8158af6.png",
                                       author_id=rand_user)