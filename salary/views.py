from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import staff
from .models import attendance
from .models import amount
import datetime


def index(request):

    staffs = staff.objects.all()
    attendances = attendance.objects.all()
    amounts = amount.objects.all()
    count_id = staff.objects.latest('id')
    date = datetime.date.today()
    if request.method == "POST" :
        for i in range(1,count_id) :
            staff_id = request.POST.get('staff_id' + i, None)
            attendances = request.POST.get('attendance' + i, None)

            date = datetime.date.today()

            ins = attendance(staff_id=staff_id, attendance=attendances, date=date)
            ins.save()
    return render(request, "salary/index.html", {'staff': staffs, 'attendance': attendances, 'amount': amounts, 'count_id': count_id, 'date': date})


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

    