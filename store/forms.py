from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'LOGIN'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni tasdiqlash'
    }))

    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'LOGIN'
            })
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Izoh...."
            })

        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emailingiz'
            }),

        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'zipcode']

        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Manzil'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shahar'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rayon'
            }),
            'zipcode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pochta raqami'
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('text', 'contact', 'email')

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Talab va shikoyat'
            }),

            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kontaktingiz'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emailingiz'
            }),
        }
