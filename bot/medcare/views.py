from django.shortcuts import render
from django.http import HttpResponse
from .models import data


# Create your views here.
def fill_data(request):
    # nam = request.GET[name]
    # quantity = request.GET(quantity)
    context = {'variable':"Rithik"}
    return render(request,'fill_data.html',context=context)

def add(request):

    val1=request.GET['name']
    val2=request.GET['quantity']
    # context = {'v1':val1,'v2':val2}
    info = data(name=val1,quantity=val2)
    info.save()

    return render(request,'redirect.html',{'v1':val1,'v2':val2})
