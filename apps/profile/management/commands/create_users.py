from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed user data'

    def handle(self, *args, **kwargs):
        data_to_add = [
            {'username': 'nadip','password': 'nadip123','email': 'nadip@gmail.com'},
            {'username': 'nopal','password': 'nopal123','email': 'nopal@gmail.com'},
            {'username': 'jalu','password': 'jalu123','email': 'jalu@gmail.com'},
        ]
        for data in data_to_add:
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            user = User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f"User '{username}' berhasil ditambahkan"))