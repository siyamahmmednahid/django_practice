from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.position + ' - ' + self.department


class Project(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=100)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.project_name + ' - ' + self.project_status