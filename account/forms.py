from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["username", "password", "is_active", "is_admin"]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={"class": "input__item", "placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"class": "input__item", "placeholder": "Your Email"}),
            "password": forms.PasswordInput(attrs={"class": "input__item", "placeholder": "Your Password"}),
        }

    def clean(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        if User.objects.filter(email=email, username=username).exists():
            raise ValidationError("Email already registered!", code="invalid_email")
        if User.objects.filter(username=username).exists():
            raise ValidationError("username already registered!", code="invalid_username")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input__item", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input__item", "placeholder": "Password"}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "profile_image")
