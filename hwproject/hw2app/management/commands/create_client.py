from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create client."
    
    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            client = Client(
                name=f'Client {i}',
                email=f'client{i}@mail.com',
                phone_num=f'+3752915947{i}{i}',
                address='Belarus, Minsk',
            )
            client.save()
            self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))