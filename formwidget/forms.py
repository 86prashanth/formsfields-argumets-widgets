from django import forms

class Registration(forms.Form):
    name=forms.CharField(widget=forms.Textarea())
    email=forms.EmailField()
    phone=forms.CharField()