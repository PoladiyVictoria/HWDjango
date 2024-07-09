from django import forms

class Product_form(forms.Form):
    name = forms.CharField(max_length=50, label="Введите название товара")
    description = forms.CharField(label="Описание товара")
    price = forms.DecimalField(max_digits=200, decimal_places=2, label="Цена товара")
    quantity = forms.IntegerField(label="Количество товара")
    image = forms.ImageField(label="Фото товара", widget=forms.FileInput(attrs={"class": "form-control", "type": "file"}))
    
class Get_Product(forms.Form):
    name = forms.CharField(max_length=50, label="Введите название товара")