from django.shortcuts import render
from testapp.models import Employee

def empinfo(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/demo.html',context=my_dict)