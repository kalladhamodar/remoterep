from django.shortcuts import render
from .models import productdata
from .forms import insertingdata,updatingdata,deletingdata
from django.http.response import HttpResponse
def indexview(request):
    return render(request,'index.html')
def insertingview(request):
    if request.method=="POST":
        iform=insertingdata(request.POST)
        if iform.is_valid():
            name=request.POST.get('name')
            Address=request.POST.get('address')
            Constituecy=request.POST.get('Constituecy')
            District=request.POST.get('District')
            mobile=request.POST.get('mobile')
            state=request.POST.get('state')
            data=productdata(name=name,Address=Address,Constituecy=Constituecy,District=District,mobile=mobile,state=state)
            data.save()

            iform=insertingdata()
            return render(request,'inserting.html',{'iform':iform})
        else:
            return HttpResponse("user invalid data")
    else:
        iform = insertingdata()
        return render(request, 'inserting.html', {'iform': iform})

def retriveview(request):
    products=productdata.objects.all()
    return render(request,'retriving.html',{'products':products})
def updatingview(request):
    if request.method=="POST":
        uform=updatingdata(request.POST)
        if uform.is_valid():
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pdata=productdata.objects.filter(name=name)
            if pdata:
                pdata.update(mobile=mobile)
                uform=updatingdata()
                return render(request,'updating.html',{'uform':uform})
            else:
                return HttpResponse("invalid name")
        else:
            return HttpResponse("invalid data")
    else:
        uform = updatingdata()
        return render(request, 'updating.html', {'uform': uform})

def deletingview(request):
    if request.method=="POST":
        dform=deletingdata(request.POST)
        if dform.is_valid():
            name=request.POST.get('name')
            pdata=productdata.objects.filter(name=name)
            if pdata:
                pdata.delete()
                dform=updatingdata()
                return render(request,'deleting.html',{'dform':dform})
            else:
                return HttpResponse("invalid name")
        else:
            return HttpResponse("invalid data")
    else:
        dform = updatingdata()
        return render(request, 'deleting.html', {'dform': dform})









