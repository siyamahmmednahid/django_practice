from django.urls import path
from office import views


app_name = 'office'

urlpatterns = [
    path('', views.index, name='index'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('employeeDetails/<int:employee_id>/', views.employeeDetails, name='employeeDetails'),
    path('editEmployee/<int:employee_id>/', views.editEmployee, name='editEmployee'),
    path('deleteEmployee/<int:employee_id>/', views.deleteEmployee, name='deleteEmployee'),
    path('addProject/<int:employee_id>/', views.addProject, name='addProject'),
    path('projectDetails/<int:project_id>/', views.projectDetails, name='projectDetails'),
    path('updateProject/<int:project_id>/', views.updateProject, name='updateProject'),
    path('deleteProject/<int:project_id>/', views.deleteProject, name='deleteProject'),
    path('testURL/', views.testURL, name='testURL'),
]