from cProfile import label
from django.shortcuts import render
from .forms import RegisterForm,FormField
# Create your views here.

def home(request):
    form=RegisterForm(auto_id='sakiye',label_suffix='')
    return render(request,'app/labelsuffix.html',{'form':form})

def order(request):
    form=RegisterForm()
    form.order_fields(field_order=['email','mobile','name'])
    return render(request,'app/order.html',{'form':form})

def loop(request):
    form=RegisterForm()
    return render(request,'app/loopform.html',{'form':form})

def formfield(request):
    form=RegisterForm()
    return render(request,'app/formfield.html',{'form':form})

def arg(request):
    form=FormField(initial={'name':'rahul'})
    return render(request,'app/formfield arg.html',{'form':form})
