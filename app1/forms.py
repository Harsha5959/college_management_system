from django import forms
from .models import Department, HOD, Professor, Student


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class HODForm(forms.ModelForm):
    class Meta:
        model = HOD
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
