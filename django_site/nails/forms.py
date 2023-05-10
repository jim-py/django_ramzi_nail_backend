from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    username = forms.CharField(error_messages={'unique': 'Этот номер телефона занят!'}, label='Телефон', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Телефон', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UsersUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label='Имя', max_length=100, widget=forms.TextInput())
    telephone = forms.IntegerField(required=False, label='Телефон', widget=forms.NumberInput())

    class Meta:
        model = User
        fields = ['first_name', 'telephone']
        widgets = {
            'role': forms.Select(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}),
            'status': forms.Select(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}),
        }


# class UsersAddForm(UserCreationForm):
#     last_name = forms.CharField(required=False, label='Фамилия', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     first_name = forms.CharField(required=False, label='Имя', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     middle_name = forms.CharField(required=False, label='Отчество', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     city = forms.CharField(required=False, label='Город', max_length=50, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     road = forms.CharField(required=False, label='Улица', max_length=50, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     house = forms.CharField(required=False, label='Дом', max_length=10, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     telephone = forms.IntegerField(required=False, label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     username = forms.CharField(required=False, label='Логин', max_length=30, help_text='', widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#
#     class Meta:
#         model = User
#         fields = ['role', 'status', 'last_name', 'first_name', 'middle_name', 'city', 'road', 'house', 'telephone', 'username']
#         widgets = {
#             'role': forms.Select(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}),
#             'status': forms.Select(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}),
#         }
#
#
# class ProfileForm(forms.ModelForm):
#     last_name = forms.CharField(required=False, label='Фамилия', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     first_name = forms.CharField(required=False, label='Имя', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     middle_name = forms.CharField(required=False, label='Отчество', max_length=100, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     city = forms.CharField(required=False, label='Город', max_length=50, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     road = forms.CharField(required=False, label='Улица', max_length=50, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     house = forms.CharField(required=False, label='Дом', max_length=10, widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     telephone = forms.IntegerField(required=False, label='Номер телефона', widget=forms.NumberInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#     username = forms.CharField(required=False, label='Логин', max_length=30, help_text='', widget=forms.TextInput(attrs={'class': 'w-25 fs-3 form-control bg-dark text-light'}))
#
#     class Meta:
#         model = User
#         fields = ['last_name', 'first_name', 'middle_name', 'city', 'road', 'house', 'telephone', 'username']
