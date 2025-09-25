
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field


# ---------------- Custom Signup Form ---------------- #

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Remove help texts from Django's defaults

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        # Add Bootstrap classes for styling

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# ---------------- Contact Form ---------------- #

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-md-3 col-form-label text-end'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Row('name'),
            Row('email'),
            Row('message'),
        )


  
