from django import forms
from .models import marklist
class StudentForm(forms.ModelForm):
    class Meta:
        model = marklist
        fields = "__all__"