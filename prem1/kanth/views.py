# from unicodedata import name
# from django.shortcuts import render
# from django.db.models import Q
# from django.db.models.aggregates import Max,Min,Sum,Count,Avg

# # Create your views here.
# from kanth.models import rb,real,somu

# def somu1(request):
#     res=somu.objects.all()
#     # res=somu.objects.filter(name='ramesh')
#     # res=somu.objects.filter(Q(name='ramesh'))
#     # res=somu.objects.exclude(name=['rock','prem'])
#     # res=somu.objects.filter(name__in=['rock','sri'])
#     # res=somu.objects.exclude(name__in=['rock','nagu'])
#     # res=somu.objects.filter(age__range=[20,35])
#     # res=somu.objects.exclude(age=54)
#     # res=somu.objects.filter(name__contains='r')
#     # res=somu.objects.exclude(name__icontains='M')
#     # res=somu.objects.filter(name__istartswith='r')
#     # res=somu.objects.filter(name__istartswith='i')
#     # res=somu.objects.filter(name__iendswith='k')
#     # res=somu.objects.exclude(name__iexact='rock')
#     # res=somu.objects.filter(name__exact='rock')
#     # res=somu.objects.filter(age__range=[1,50])
#     # res=somu.objects.all().order_by('name')
#     # res=somu.objects.all().aggregate(Max('age'))
#     # res=somu.objects.only('email')
#     # res=somu.objects.only('name','age')
#     # res=somu.objects.all()[3:4]
    

#     return render(request,'display.html',{'res':res})

# def real1(request):
#     res=real.objects.all()
#     return render(request,'display1.html',{'res':res})

# def rb1(request):
#     res=rb.objects.all()
#     return render(request,'display2.html',{'res':res})

