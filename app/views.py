from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from app.forms import *

def insert_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid = SFDO.cleaned_data['Sid']
            Semail = SFDO.cleaned_data['Semail']

            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
            return HttpResponse('Data insert successfully...')
    return render(request,'insert_student.html',d)