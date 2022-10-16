from .forms import Registration
from django.shortcuts import render
from django.http import HttpResponseRedirect


def success(request):
    return render(request,'app/success.html')

def home(request):
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            print("form is validated")
            print("name:",form.cleaned_data['name'])
            print("email:",form.cleaned_data['email'])
            print("password:",form.cleaned_data['password'])
            form=Registration()
            return HttpResponseRedirect('success')
            
    else:
        form=Registration()
    return render(request,'app/getform data.html',{'form':form})