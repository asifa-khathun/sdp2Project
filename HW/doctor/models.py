# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class Doctor(models.Model):
    demail=models.EmailField()    
    dname=models.CharField(max_length=100)
    dage=models.CharField(max_length=3)
    dgender=models.CharField(max_length=7)
    dexperience=models.CharField(max_length=10)
    dcontact=models.CharField(max_length=15)
    dpsw=models.CharField(max_length=15)
    donduty=models.CharField(max_length=5)
    dspec=models.CharField(max_length=30)
    class Meta:
        db_table = "doctor"
