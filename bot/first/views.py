from django.shortcuts import render
from first.models import medicine


def login(request):
    return render(request,'login.html')

def check(request):
    val1 = (request.GET['user'])
    val2 = (request.GET['pass'])
    if(val1 == 'rithik' and val2 == '1234'):
        return render(request,'nav.html')
    else:
        return render(request,'login.html')


def select(request):
    go=request.GET['enter']
    if(go=="add"):
        return render(request,'add_data.html')
    else:
        new_medicine=medicine.objects.all()
        return render(request,'table.html')

def add_data(request):
    name = request.GET['name']
    quantity = request.GET['quantity']
    desc = request.GET['desc']
    comp = request.GET['comp']
    med = medicine(name=name,quantity=quantity,desc=desc,comp=comp)
    med.save()
    new_medicine=medicine.objects.all()
    return render(request,'table.html',{'new_medicine': new_medicine})


    
    # return render(request,'add_data.html')

# def show(request):
  


