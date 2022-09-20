from unicodedata import name
from django.shortcuts import render
from office.forms import EmployeeForm, ProjectForm
from office.models import Employee, Project
from django.http import JsonResponse

# Create your views here.

# For Home Page
def index(request):
    employee_list = Employee.objects.order_by('name')
    homeDict = {'title': 'Home Page', 'employee_list': employee_list}
    return render(request, 'office/index.html', context=homeDict)


# For Add Employee Page
def addEmployee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    addEmployeeDict = {'title': 'Add Employee', 'form': form}
    return render(request, 'office/addEmployee.html', context=addEmployeeDict)


# For Employee Details Page
def employeeDetails(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    project_list = Project.objects.filter(name=employee_id)
    employeeDict = {'title': 'Employee Details', 'employee': employee, 'project_list': project_list}
    return render(request, 'office/employeeDetails.html', context=employeeDict)

# For Edit Employee Page
def editEmployee(request, employee_id, path):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return employeeDetails(request, employee_id)

    editEmployeeDict = {'title': 'Edit Employee', 'form': form}
    return render(request, 'office/editEmployee.html', context=editEmployeeDict)


# For Add Project Page
def addProject(request, employee_id):
    form = ProjectForm(initial={'name': employee_id})

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return employeeDetails(request, employee_id)

    addProjectDict = {'title': 'Add Project', 'form': form}
    return render(request, 'office/addProject.html', context=addProjectDict)



def testURL(request):
    Employee_list = Employee.objects.order_by('name')
    return JsonResponse({'Employee_list': list(Employee_list.values())})