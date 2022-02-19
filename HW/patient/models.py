from django.db import models
from django.core.validators import FileExtensionValidator

class Patient(models.Model):
	pname=models.CharField(max_length=100)
	pemail=models.EmailField()
	page=models.CharField(max_length=3)
	pgender=models.CharField(max_length=7)
	pcontact=models.CharField(max_length=15)
	ppsw=models.CharField(max_length=15)
	ppres=models.FileField(upload_to='files/',validators=[FileExtensionValidator(['pdf'])])
	class Meta:
		db_table = "patient"
