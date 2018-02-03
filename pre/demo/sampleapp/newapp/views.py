from django.shortcuts import render
from newapp.models import Student
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request,"Home.html",
                  {'Students':Student.objects.all()})

import json
@csrf_exempt
def RegisterStudent(request):
    if(request.method=='POST'):
        d=request.POST
        Name = d.get("StudentName", "0")
        Email = d.get("StudentEmail", "0")
        contact_number = d.get("StudentContactNumber", "0")
        Student.objects.create(name=Name,email=Email,Contact_Number=contact_number)
        return home(request)
    return render(request,"RegisterStudent.html")