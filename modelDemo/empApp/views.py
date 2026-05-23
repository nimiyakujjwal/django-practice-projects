from django.shortcuts import render
from .models import Employee

# Create your views here.
def EmployeeView(request):
    employees = Employee.objects.all()
    empDict = {'employees': employees}
    return render(request, 'empApp/employee_list.html', empDict)
