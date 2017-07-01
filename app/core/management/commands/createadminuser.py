# ! coding: utf-8

from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = 'Starts the Admin user.'

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='admin@djcodingtest.com', password='password')
