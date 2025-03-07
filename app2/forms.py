from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=11, required=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'phone','password1','password2')

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="ایمیل") 

    def clean_username(self):
        email = self.cleaned_data.get('username')
        try:
            validate_email(email)  
        except ValidationError:
            raise forms.ValidationError("لطفاً یک ایمیل معتبر وارد کنید.")
        return email