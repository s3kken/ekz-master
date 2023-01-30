from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User, Product


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar')


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image')
