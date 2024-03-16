from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        fields = '__all__'

    def save(self):
        data = self.cleaned_data
        data.pop('password2')
        user = User(**data)
        user.set_password(data['password'])
        user.save()
        return user
