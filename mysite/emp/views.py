from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import emp
# Create your views here.


def emp_home(request):
    # return HttpResponse("Student home")

    emps = emp.objects.all()

    return render(request, "emp/home.html", {'emps':emps})


def addEmp(request):
    if request.method == 'POST':
        # print('data is comming...')
        # data fetch
        empName = request.POST.get('empName')
        empEmail = request.POST.get('empEmail')
        empId = request.POST.get('empId')
        empPhone = request.POST.get('empPhone')
        empAddress = request.POST.get('empAddress')
        empDepartment = request.POST.get('empDepartment')
        empWorking = request.POST.get('empWorking')

        # validate

        # create model object and set the data
        e = emp()
        e.name = empName
        e.email = empEmail
        e.empId = empId
        e.phone = empPhone
        e.address = empAddress
        e.department = empDepartment
        if empWorking==None:
            e.working = False
        else:
            e.working = True

        # save the data
        e.save()

        # prepare message

        return redirect('/emp/home/')
    return render(request, 'emp/addEmp.html', {})



def deleteEmp(request, empId):
    emp.objects.get(id=empId).delete()
    return redirect('/emp/home/')


def updateEmp(request, empId):
    Emp = emp.objects.get(id=empId)
    return render(request, 'emp/updateEmp.html', {'emp':Emp})


def do_update_emp(request, emp_Id):
    if request.method == 'POST':
        empName = request.POST.get('empName')
        empEmail = request.POST.get('empEmail')
        empId = request.POST.get('empId')
        empPhone = request.POST.get('empPhone')
        empAddress = request.POST.get('empAddress')
        empDepartment = request.POST.get('empDepartment')
        empWorking = request.POST.get('empWorking')

        e = emp.objects.get(id=emp_Id)

        e.name = empName
        e.email = empEmail
        e.empId = empId
        e.phone = empPhone
        e.address = empAddress
        e.department = empDepartment
        if empWorking==None:
            e.working = False
        else:
            e.working = True

        e.save()

    return redirect('/emp/home/')


