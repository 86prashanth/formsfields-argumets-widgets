from cProfile import label
from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(initial="prashanth",help_text="it field name have 30 characters")
    email=forms.EmailField()
    mobile=forms.IntegerField()
    key=forms.CharField(widget=forms.HiddenInput())
    
    
class FormField(forms.Form):
    name=forms.CharField(label="Your name",label_suffix='',initial="your name..",required=False,disabled=True,help_text='limit 70 characters')