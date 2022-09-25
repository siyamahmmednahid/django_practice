from django.urls import path
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('student_detail/<pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student_create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student_update/<pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('subject_detail/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
]