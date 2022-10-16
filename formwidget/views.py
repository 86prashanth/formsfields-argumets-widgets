from django.shortcuts import render
from .forms import Registration
# Create your views here.
def home(request):
    form=Registration()
    return render(request,'app/widget.html',{'form':form})