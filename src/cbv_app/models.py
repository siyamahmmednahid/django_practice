from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    batch = models.CharField(max_length=50)
    roll = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.roll) + " - " + self.batch
    def get_absolute_url(self):
        return reverse("cbv_app:student_detail", kwargs={"pk": self.pk})
    


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=50)
    subject_credit = models.IntegerField()

    def __str__(self):
        return self.subject_name + " - " + self.subject_code + " - " + str(self.subject_credit)
