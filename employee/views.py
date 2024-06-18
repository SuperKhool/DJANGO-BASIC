from django.http import HttpResponse, Http404
from django.shortcuts import render , get_object_or_404

from employee.models import Employee

# Create your views here.

def employees_detail(request ,pk ):
    employee=get_object_or_404(Employee,pk=pk)
    contex={
        'employee':employee
    }
    return render(request,'employee_detail/detail.html',contex)

    #try :
        #employee=Employee.objects.get(pk=pk)
        #return HttpResponse(employees_detail)
    #except:
        #raise Http404