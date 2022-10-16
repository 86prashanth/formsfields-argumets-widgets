from django import forms

class Registration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField()