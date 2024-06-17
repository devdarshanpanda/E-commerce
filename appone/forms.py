from django import forms
from appone.models import Contact,Address
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class CustomerRegistrationForm(UserCreationForm):

    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))
    email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={"class":"form-control form-control-lg"}))
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]
    

    
class Login_form(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))


class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields ="__all__"
        widgets={
            "full_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "message":forms.Textarea(attrs={"class":"form-control"}),
            }


class Addressform(forms.ModelForm):
    class Meta:
        model= Address
        fields=['street', 'city', 'state', 'zipcode',"phone","name"]
        widgets={"name":forms.TextInput(attrs={"class":"form-control"}),
                 "street":forms.TextInput(attrs={"class":"form-control"}),
                 "city":forms.TextInput(attrs={"class":"form-control"}),
                 "phone":forms.NumberInput(attrs={"class":"form-control"}),
                 "zipcode":forms.NumberInput(attrs={"class":"form-control"}),
                 "state":forms.TextInput(attrs={"class":"form-control"})
                 }
        

# class Addressform(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['street', 'city', 'state', 'zipcode',"phone","name"]