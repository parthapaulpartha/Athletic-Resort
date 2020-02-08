from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from .models import notepad

# ----------- Registration Form --------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

# ----------- Log in Form --------
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

# ----------- Edit Profile Form --------
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

# ----------- Note pad Form --------
class NotePadForm(forms.ModelForm):
    class Meta:
        model = notepad
        fields = [
            'note_pad',
        ]