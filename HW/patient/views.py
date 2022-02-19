# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from patient.forms import PatientForm
from patient.models import Patient
from doctor.forms import DoctorForm
from doctor.models import Doctor
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def patdab(request):
    return render(request, "patdab.html",{'id':id})

def pat(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,"patlogin.html")
            except:
                pass
    else:
        form = PatientForm()
    return render(request,'patient.html',{'form':form})
def patlogin(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            pemail=form.data["pemail"]
            dspw=form.data["pspsw"]
            flag=Patient.objects.filter(pemail=pemail,ppsw=ppsw)
            id=Patient.objects.get(pemail=pemail,ppsw=ppsw).id
            #request.session['id']=id
            if flag:
                request.session['pemail']=pemail
                return render(request, "patdab.html",{'id':id})
            else:
                return render(request,"patlogin.html")
    else:
        form = PatientForm()
    return render(request,'patlogin.html',{'form':form})
    
def patedit(request, id):
    request.session["id"]=id
    return render(request,'patedit.html',{'id':id})
 
def patupdate(request):
    id=request.session["id"]
    #form=DoctorForm(request.POST, instance=doctor)
    if request.method=="POST":
        pemail=request.Post["pemail"]
        pname=request.POST["pname"]
        pcontact=request.POST["pcontact"]
        Patient.objects.filter(id=id).update(pemail=pemail,pname=pname,pcontact=pcontact)
        return render(request, 'patdab.html')
    else:
        return render(request, 'patdab.html')

def patdestroy(request, id):
    patient=Patient.objects.get(id=id)
    patient.delete()
    return redirect('patlogin')

def consult(request):
    doctors=Doctor.objects.all()
    return render(request,'consult.html',{'doctors':doctors})

def uploadpres(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form1.save()
            return redirect("patdab")
    else:
        form=PatientForm()
    return render(request, "uploadpres.html",{'form':form})

def viewppres(request):
    patients=Patient.objects.all()
    #count=File.objects.all()
    return render(request,'viewfiles.html',{'patients':patients})

def medicines(request):
    return render(request, 'medicines.html')

def services(request):
    return render(request, 'services.html')

def test(request):
    return render(request, 'test.html')