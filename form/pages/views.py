from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password
from pages.models import employee
from django.utils.datastructures import MultiValueDictKeyError
from django.forms import ValidationError
from . import forms

def index(request):
    #fetching form data
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        try:
            ispublic = request.POST['ispublic']
        except MultiValueDictKeyError:
            ispublic = False
        #server side Validations

        if username == "":
         raise ValidationError("Username must be filled out")
        if ispublic==False:
         raise ValidationError("Select any option")

        # storing data to the database
        ins = employee(name=name, username=username, password=password, ispublic=ispublic)
        ins.password = make_password('password')
        ins.save()
    return render(request, 'form.html')



