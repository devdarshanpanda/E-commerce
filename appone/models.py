from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.BigIntegerField()
    message=models.TextField()

CATEGORY_CHOICE=(
    ("M","Mobile"),
    ("L","Laptop"),
    ("TW","Top Were"),
    ("BW","Bottom Were"),
)

STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('packed','Packed'),
    ('One_the_way','On The WAY'),
    ('Delivered','Delivered'),
)

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICE, max_length=10)
    brand=models.CharField( max_length=50)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField(max_length=300)
    img=models.ImageField(upload_to="product/")



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=50)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


class Order_placed(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    products=models.ForeignKey(Products, on_delete=models.CASCADE)
    status=models.CharField(choices=STATUS_CHOICE,max_length=50,default="Pending")
    