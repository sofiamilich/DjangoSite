from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Password')
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Repeat Password')
    age = forms.IntegerField(min_value=18, max_value=120, label='Age')