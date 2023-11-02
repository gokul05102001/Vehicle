from django.shortcuts import render,redirect
from .models import vehicles
from .forms import vehicleform
# Create your views here.
def home(request):
    Vehicles=vehicles.objects.all()
    context={
        'vehicle_list':Vehicles
    }
    return render(request,'home.html',context)

def details(request,vehicles_id):
    Vehicles=vehicles.objects.get(id=vehicles_id)
    return render(request,'details.html',{'vehicle':Vehicles})

def add_vehicle(request):
    if request.method=='POST':
        image=request.POST.get('image')
        company=request.POST.get('company')
        price=request.POST.get('price')
        features=request.POST.get('features')
        vehicle=vehicles(image=image,company=company,price=price,features=features)
        vehicle.save()
        return redirect('/')
    return render(request,'add.html')
def updates(request,id):
    Vehicles=vehicles.objects.get(id=id)
    form=vehicleform(request.POST or None,request.FILES,instance=Vehicles)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'updates.html',{'form':form,'vehicle':Vehicles})

def delete(request,id):
    if request.method=='POST':
       veHicle=vehicles.objects.get(id=id)
       veHicle.delete()
       return redirect('/')
    return render(request,'delete.html')