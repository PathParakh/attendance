from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import staff
import datetime
# Create your views here.
def index(request):
    return render(request, "salary/index.html")
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

    