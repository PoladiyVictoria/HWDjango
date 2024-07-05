from django.core.management.base import BaseCommand
from hw2app.models import Client, Product, Order
import random



class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            buyer = Client.objects.get(id=i)
            prods = []
            prods = [Product.objects.get(id=random.randint(1,9)) for _ in range(3)]
            order = Order.objects.create(client=buyer)
            order.order.add(*prods)
            order.calculate_total()
            order.save()

        self.stdout.write(self.style.SUCCESS("Fake orders is added"))