 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from doctor.forms import DoctorForm
from doctor.models import Doctor
from patient.forms import PatientForm
from patient.models import Patient
#from django.db models import Q

def docdab(request):
    return render(request, "docdab.html",{'id':id})

def doc(request):
    id=request.session["id"]
    if request.method=="POST":
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html")
    else:
        form = DoctorForm()
    return render(request,'register.html',{'form':form,'id':id})

def doclogin(request):
    if request.method=="POST":
        form=DoctorForm(request.POST)
        if form.is_valid():
            demail=form.data["demail"]
            dpsw=form.data["dpsw"]
            flag=Doctor.objects.filter(demail=demail,dpsw=dpsw)
            id=Doctor.objects.get(demail=deamil,dpsw=dpsw).id
            print(id)
            if flag:
                request.session['demail']=demail
                return render(request, "docdab.html",{'id':id})
            else:
                return render(request,"login.html")
            return render(request, "login.html")
    else:
        form = DoctorForm()
    return render(request,'login.html',{'form':form})

def show(request):
    id=request.session["id"]
    doctors=Doctor.objects.all()
    return render(request,'doconduty.html',{'doctors':doctors,'id':id})
    
def docedit(request, id):
    request.session["id"]=id
    doctor=Doctor.objects.get(id=id)
    return render(request,'edit.html',{'id':id,'doctor':doctor})
 
def docupdate(request):
    id=request.session["id"]
    #form=DoctorForm(request.POST, instance=doctor)
    if request.method=="POST":
        demail=request.Post["demail"]
        dname=request.POST["dname"]
        dexperience=request.POST["dexperience"]
        dcontact=request.POST["dcontact"]
        donduty=request.POST["donduty"]
        Doctor.objects.filter(id=id).update(demail=demail,dname=dname,dexperience=dexperience,dcontact=dcontact,donduty=donduty)
        return redirect("docshow")
    else:
        return redirect("docshow")

def docdestroy(request, id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('docshow')

def patshow(request):
    patients=Patient.objects.all()
    return render(request, 'patshow.html',{'patients':patients})