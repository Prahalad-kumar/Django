from django.shortcuts import render,redirect
from login.models import Patient,Doctor
def add_patient(request):
    if request.method=='POST':
        data=request.POST
        Patient.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            dob=data.get("dob"),
            mobile_num=data.get("mobile_num"),
            address=data.get("address"),
        )   
        return redirect('home')
    return render(request,'add_patient.html')
def add_doctor(request):
    if request.method=='POST':
        data=request.POST
        Doctor.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            specialization=data.get("specialization"),
            mobile_num=data.get("mobile_num"),
            address=data.get("address"),
        )   
        return redirect('home')
    return render(request,'add_doctor.html')
def home(request):
    return render(request,'home.html')
def show_doctors(request):
    doctors=Doctor.objects.all()
    return render(request,'show_doctors.html',{'doctors':doctors})
def show_patients(request):
    patients=Patient.objects.all()
    return render(request,'show_patient.html',{'patients':patients})

def doctors(request):
    doctors=Doctor.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})

def consultancy(request):
    return render(request,'consultancy.html')