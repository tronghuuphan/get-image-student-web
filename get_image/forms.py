from django import forms

class UserForm(forms.Form):
    mssv = forms.CharField(max_length=10)

