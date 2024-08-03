from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def home(request):
    return render(request, 'home.html')