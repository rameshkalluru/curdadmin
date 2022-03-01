from django.shortcuts import render

# Create your views here.
from app.forms import sukku_mar

def display(request):
    form=sukku_mar()
    if request.method=='post':
        form=sukku_mar(request.post)
        form.save()

    return render(request,'display.html',{'form':form})