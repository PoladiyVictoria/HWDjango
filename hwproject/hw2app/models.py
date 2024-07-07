from decimal import Decimal
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=13)
    address = models.CharField(max_length=150)
    date_reg = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Name: {self.name}, email: {self.email}"
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=200, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    add_date = models.DateField(auto_now_add=True)
    path_to_image = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"
    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=200, decimal_places=2, default=0)
    order_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Client: {self.client}, order: {self.order}"
    
    def calculate_total(self):
        total = Decimal(0)
        for product in self.order.all():
            total += product.price
        self.total_amount = total
    
