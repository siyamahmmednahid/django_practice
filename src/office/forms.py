from django import forms
from office.models import Employee, Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'position': 'Position',
            'department': 'Department',
            'salary': 'Salary',
            'address': 'Address',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'name': 'Name',
            'project_name': 'Project Name',
            'project_description': 'Project Description',
            'project_start_date': 'Project Start Date',
            'project_end_date': 'Project End Date',
            'project_status': 'Project Status',
        }
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_description': forms.TextInput(attrs={'class': 'form-control'}),
            'project_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_status': forms.TextInput(attrs={'class': 'form-control'}),
        }