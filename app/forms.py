from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from .validators import validate_email_unique, validate_username_unique


class SignUpFormUser(UserCreationForm):

    username = forms.CharField(
        max_length=100,
        label='Username',
        required=True,
        validators=[validate_username_unique],
        widget=forms.TextInput(
            attrs={
                'class': 'signupForm',
                'placeholder': 'Enter your username.'
            })
    )

    email = forms.EmailField(
        required=True,
        label='Email address',
        validators=[validate_email_unique],
        widget=forms.EmailInput(attrs={
            'class': 'signupForm',
            'placeholder': 'Enter your valid email addres.'
        })
    )

    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'signupForm',
            'placeholder': 'Min 8 characters.'
        })
    )

    password2 = forms.CharField(
        required=True,
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'signupForm',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'edit_username form-profile',
            'placeholder': 'Enter your username'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'edit_email form-profile',
            'placeholder': 'Enter your valid email address'
        })
    )

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'edit_first_name form-profile',
            'placeholder': 'Enter your firstname'
        })
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'edit_last_name form-profile',
            'placeholder': 'Enter your lastname'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class UpdateUserAvatar(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'image-upload'
        })
    )

    class Meta:
        model = UserProfile
        fields = [
            'image'
        ]


class PredictForm(forms.ModelForm):
    fixed_acidity = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'fixed_acidity',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    volatile_acidity = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'volatile_acidity',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    citric_acid = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'citric_acid',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    residual_sugar = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'residual_sugar',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    chlorides = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'chlorides',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    free_sulfur_dioxide = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'free_sulfur_dioxide',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    total_sulfur_dioxide = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'total_sulfur_dioxide',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    density = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'density',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    pH = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'pH',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    sulphates = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'sulphates',
            'class': 'form-predict',
            'step': '0.1'
        })
    )

    alcohol = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'id': 'alcohol',
            'class': 'form-predict',
            'step': '0.1'
        })
    )
