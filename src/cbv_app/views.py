from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from cbv_app.models import Student, Subject
from django.urls import reverse_lazy

# Create your views here.
# For Student List View
class IndexView(ListView):
    template_name = 'cbv_app/index.html'
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context



# For Student Detail View
class StudentDetailView(DetailView):
    template_name = 'cbv_app/studentDetail.html'
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context



# For Student Create View
class StudentCreateView(CreateView):
    template_name = 'cbv_app/studentCreate.html'
    model = Student
    fields = ['name', 'email', 'phone', 'batch', 'roll']



# For Student Update View
class StudentUpdateView(UpdateView):
    template_name = 'cbv_app/studentUpdate.html'
    model = Student
    fields = ['name', 'email', 'phone', 'batch', 'roll']



# For Student Delete View
class StudentDeleteView(DeleteView):
    template_name = 'cbv_app/studentDelete.html'
    model = Student
    success_url = reverse_lazy('cbv_app:index')
    


# For Subject Detail View
class SubjectDetailView(DetailView):
    template_name = 'cbv_app/subjectDetail.html'
    model = Subject
    context_object_name = 'subject'