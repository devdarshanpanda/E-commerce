from django.shortcuts import render,redirect
from appone.models import Contact,Products,Address,Cart,Order_placed
from appone.forms import CustomerRegistrationForm,Login_form,ContactForm,Addressform
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages

# from django.http import HttpResponseRedirect

# Create your views here.
# =============================================
# index
# ========================================
def index(request):
    # Product
    top_were=Products.objects.filter(category="TW")
    bottom_were=Products.objects.filter(category="BW")
    mobile=Products.objects.filter(category="M")
    laptop=Products.objects.filter(category="L")

    contact=ContactForm()
    
    return render(request,'index.html',{"contact":contact,"top_were":top_were,"bottom_were":bottom_were,"mobile":mobile,"laptop":laptop})
#  ===================================================================================

# contact
#  ===================================================================================
def contactform(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return redirect("/")
# =================================================================   

# profile 
# =================================================================   
class Profile_view(View):
    def get(self,request):
        form=Addressform()
        if request.user.is_authenticated:
            user=request.user
            address=Address.objects.filter(user=user)
        return render(request,"profile.html",{"form":form,'address':address})
    
    def post(self,request):
        form=Addressform(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            street=form.cleaned_data['street']
            city=form.cleaned_data['city']
            phone=form.cleaned_data['phone']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            data=Address.objects.create(user=user,name=name,street=street,city=city,phone=phone,zipcode=zipcode,state=state)
            return redirect("profile")
    
# =================================================================   
# signup 
# =================================================================   

class signup(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"signup.html" ,{"form":form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            return redirect("/")
        return render(request,"signup.html",{"form":form})
        # return redirect("index")
    
# ========================================================
# login 
# ========================================================
def user_login(request):
    if request.method == "POST":
        form=Login_form(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=uname,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form=Login_form()
    return render(request,'login.html',{'form':form})
# =============================================================================
# logout 
# =============================================================================
def logout(request):
    auth_logout(request)
    return redirect("/")
# =====================================================
# cart
# =====================================================
def cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart_data=Cart.objects.filter(user=user)
        sub_total=0
        total=0
        for i in cart_data:
            sub_total+=i.product.selling_price
        total=sub_total+70
            
    return render(request,"cart.html",{"cart_data":cart_data,"sub_total":sub_total,"total":total})
    
# ======================================================
# add-to-cart 
# ======================================================
class Add_to_cart(View):
    def post(self,request):
        user=request.user
        product_id=request.POST['product_id']
        product=Products.objects.get(id=product_id)

        Cart.objects.create(user=user,product=product)

        return redirect('cart')
# ======================================================
# delete cart 
# ======================================================
def delete_cart(request,id):
    cart_id=id
    data=Cart.objects.get(id=cart_id)
    data.delete()
    return redirect("cart")
# ======================================================
# select address 
# ======================================================
def select_address(request):
    if request.user.is_authenticated:
        user=request.user
        address=Address.objects.filter(user=user)

    return render(request,"select_address.html",{'address':address})
# ======================================================
# order place
# ======================================================
def order_place(request):
    if request.user.is_authenticated:
        user=request.user
        address_id=request.GET['address']
        address=Address.objects.get(id=address_id)
        cart=Cart.objects.filter(user=user)
        for cart_instance in cart:
            Order_placed.objects.create(user=user,address=address,products=cart_instance.product)
            cart_instance.delete()
    return redirect("order")
# ======================================================
# orders page 
# ======================================================
def order(request):
    if request.user.is_authenticated:
        user=request.user
        order_data=Order_placed.objects.filter(user=user).order_by('id').reverse()


    return render(request,"orders.html",{"order_data":order_data})
# ======================================================
