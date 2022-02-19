from django import forms
from patient.models import Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('ppres', )
        widgets={ 'ppsw':forms.PasswordInput(),}