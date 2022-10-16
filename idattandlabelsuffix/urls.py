from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('order/',order,name='order'),
    path('loop/',loop,name='loop'),
    path('field/',formfield,name='field'),
    path('arg/',arg,name='argument'),
]
