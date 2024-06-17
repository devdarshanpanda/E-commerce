from django.urls import path
from appone import views

urlpatterns = [
    path('',views.index, name="index"),
    path('signup/',views.signup.as_view(),name="signup"),
    path('login/',views.user_login ,name='login'),
    path('logout/',views.logout,name="logout"),
    path('cart/',views.cart, name="cart"),
    path('contactform/',views.contactform, name="contactform"),
    path('profile/',views.Profile_view.as_view(), name="profile"),
    path("add_to_cart/",views.Add_to_cart.as_view(),name="add_to_cart"),
    path("delete_cart/<int:id>/",views.delete_cart,name="delete_cart"),
    path("select_address/",views.select_address,name="select_address"),
    path("order_place/",views.order_place,name="order_place"),
    path("order/",views.order,name="order"),
]
