from django import forms
from .models import user
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    class Meta:
        model=user
        fields=['username','first_name','last_name','email','affiliation','password1','password2']
        widgets={
            'email': forms.EmailInput(
                attrs={
                    'placeholder' : "Email universitaire"
                }
            ),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }