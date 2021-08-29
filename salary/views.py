from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import staff
from .models import attendance
from .models import amount
import datetime


def index(request):
    if request.method == "POST" :
        # for staffs in staff :
        #     stf_if = 'staff_id' + {{staffs.id}}
        #     staff_id = request.POST[stf_if]

        #     at_if = 'attendance' + {{staffs.id}}
        #     attendances = request.POST[at_if]

        #     date = datetime.date.today()

        #     ins = attendance(staff_id=staff_id, attendance=attendances, date=date)
        #     ins.save()
        staff_id = request.POST.get('staff_id1', None)
        attendances = request.POST.get('attendance1', None)

        date = datetime.date.today()

        ins = attendance(staff_id=staff_id, attendance=attendances, date=date)
        ins.save()

    # staff_id = request.POST['staff_id2']
    # attendances = request.POST['attendance2']

    # date = datetime.date.today()

    # ins = attendance(staff_id=staff_id, attendance=attendances, date=date)
    # ins.save()

    staffs = staff.objects.all()
    attendances = attendance.objects.all()
    amounts = amount.objects.all()
    count_id = staff.objects.latest('id')
    date = datetime.date.today()
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

    