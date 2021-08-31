from django.db.models.fields import DateTimeField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import staff
from .models import attendance
from .models import amount
import datetime


def index(request):

    staffs = staff.objects.all()

    a = staff.objects. values_list('id', flat=True)

    attendances = attendance.objects.all()
    amounts = amount.objects.all()
    # count_id = staff.objects.latest('id')
    date = datetime.date.today()
    if request.method == "POST" :
        for i in a :
            print(i)
            stf = 'staff_id' + str(i)
            print(stf)
            atd = 'attendance' + str(i)
            print(atd)
            staff_id = request.POST.get(stf, None)
            attendances = request.POST.get(atd, None)

            date = datetime.date.today()

            ins = attendance(staff_id=staff_id, attendance=attendances, date=date)
            ins.save()
        return HttpResponseRedirect("/index")
    date = datetime.date.today()
    return render(request, "salary/index.html", {'staff': staffs, 'attendance': attendances, 'amount': amounts, 'date': date})


def user(request):
    if request.method == "POST" :
        name = request.POST['name']
        role = request.POST['role']
        salary = request.POST['salary']
        address = request.POST['address']
        number = request.POST['number']
        date = datetime.date.today()

        ins = staff(name=name, role=role, salary=salary, address=address, date=date, number=number)
        ins.save()
    staffs = staff.objects.all()
    return render(request, "salary/user.html", {'staff': staffs})

    