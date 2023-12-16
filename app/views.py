from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def dept(request):
    
    dlop=Department.objects.all()
    d={'dept':dlop}
    return render(request,'dept.html',d)


def emp(request):
    elop=Employee.objects.all()
    d={'emp':elop}
    return render(request,'emp.html',d)

def insert_dept(request):
    dno=int(input('enter deptno'))
    dn=input('enter dname')
    lo=input('entr locn')
    ndo=Department.objects.get_or_create(DEPTNO=dno,DNAME=dn,LOC=lo)[0]
    ndo.save()
    dlop=Department.objects.all()
    d={'dept':dlop}
    return render(request,'dept.html',d)


def insert_emp(request):
    eno=int(input('enter empno'))
    en=input('enter ename')
    jo=input('enter job')
    mg=int(input('enter mgr'))
    hd=input('enter hiredate')
    sa=int(input('enter sal'))
    com=int(input('enter comm'))
    dno=int(input('enter deptno'))
    to=Department.objects.get(DEPTNO=dno)
    neo=Employee.objects.get_or_create(EMPNO=eno,ENAME=en,JOB=jo,MGR=mg,HIREDATE=hd,SAL=sa,COMM=com,DEPTNO=to)[0]
    neo.save()
    elop=Employee.objects.all()
    d={'emp':elop}
    return render(request,'emp.html',d)
    
