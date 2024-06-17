from django.contrib import admin
from appone.models import Products,Contact,Address,Cart,Order_placed
# Register your models here.



class Showproducts(admin.ModelAdmin):
    list_display=['product_name',"category",'discounted_price']
class ShowContact(admin.ModelAdmin):
    list_display=['full_name',"email",'phone','message']
class ShowAddress(admin.ModelAdmin):
    list_display=['user',"name",'state',"phone"]
class ShowCart(admin.ModelAdmin):
    list_display=['user',"product",'quantity']
class ShowOrderPlaced(admin.ModelAdmin):
    list_display=['user','address',"products",'status']
   
admin.site.register(Products,Showproducts)
admin.site.register(Contact,ShowContact)
admin.site.register(Address,ShowAddress)
admin.site.register(Cart,ShowCart)
admin.site.register(Order_placed,ShowOrderPlaced)

