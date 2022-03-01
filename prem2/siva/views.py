from django.shortcuts import render

# Create your views here.

from siva.models import n1

def no(request):
    res=n1.objects.all()
    return render(request,'display.html',{'res':res})
