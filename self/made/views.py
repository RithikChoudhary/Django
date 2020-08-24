from django.shortcuts import render
# from django import request
# Create your views here.
def hey(request):
    return render(request,'hey.html')

def subtract(request):
    num =request.GET['fu']
    return render(request,'result.html',{'show':num})


print("hety")

