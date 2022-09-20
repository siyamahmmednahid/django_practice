from django.urls import path
from office import views


app_name = 'office'

urlpatterns = [
    path('', views.index, name='index'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('employeeDetails/<int:employee_id>/', views.employeeDetails, name='employeeDetails'),
    path('addProject/<int:employee_id>/', views.addProject, name='addProject'),
    path('editEmployee/<int:employee_id>/', views.editEmployee, name='editEmployee'),
    path('testURL/', views.testURL, name='testURL'),
]