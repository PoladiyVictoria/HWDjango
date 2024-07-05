from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create client."
    
    def handle(self, *args, **kwargs):
        client = Client(
            name='Victoria',
            email='victory@mail.com',
            phone_num='+375291594769',
            address='Belarus, Minsk',
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))