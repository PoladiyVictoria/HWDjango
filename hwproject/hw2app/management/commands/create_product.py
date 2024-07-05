from django.core.management.base import BaseCommand
from hw2app.models import Product


class Command(BaseCommand):
    help = "Create product."
    
    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            product = Product(
                name=f'Product {i}',
                description=f'Description {i}',
                price=i * 1.2,
                quantity=i + 2,
            )
        product.save()
        self.stdout.write(self.style.SUCCESS(f"Some fake test product is created"))