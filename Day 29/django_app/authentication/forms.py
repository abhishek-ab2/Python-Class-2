from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        fields = '__all__'

    def clean_username(self):
        value = self.cleaned_data.get('username')
        return value

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password2'):
            self.add_error('password2', 'Confirm doesn\'t match')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password2')
        user = User(**data)
        user.set_password(data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = '__all__'

    def save(self):
        data = self.cleaned_data
        return authenticate(**data)
