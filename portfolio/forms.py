from django import forms
from .models import *



#create form class
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'email_address', 'phone_number', 'message')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+8801xxxxxxxxx...'}),
            'message': forms.Textarea(attrs={'class': 'form-control message-form', 'placeholder': 'Enter your message here...', 'rows': '10'}),
        }


