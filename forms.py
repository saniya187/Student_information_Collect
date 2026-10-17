from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','course','age']
        widgets = {
            'name':forms.TextInput(attrs={"placeholder":"Enter Student Name"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Email Address"}),
            'course':forms.TextInput(attrs={"placeholder":"Enter Cource"}),
            'age':forms.NumberInput(attrs={"placeholder":"Enter Age",'min':10})        
        }
   