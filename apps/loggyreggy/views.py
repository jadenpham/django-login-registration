from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import User
import bcrypt


def index(request):
    return render(request, 'loggyreggy/index.html')

def reggy(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        context = {
            "user_info" : User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashedpw)
        }
        request.session['user_id'] = context['user_info'].id
        return redirect('/success')

def login(request):
    # errors = User.objects.b(request.POST)
    # if len(errors) > 0:
    #     for key, value, in errors.items():
    #         messages.error(request, value)
    #     return redirect('/') 
    user =User.objects.filter(email = request.POST['email']) #gives back list of dict
    if len(user) < 1:
        messages.error(request, "Invalid login")
        return redirect('/')
    if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
        request.session['user_id'] = user[0].id #calling first obj in list
        return redirect('/success')
    else:
        messages.error(request, "Invalid Login")
        return redirect('/')
    

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render (request, 'loggyreggy/success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')





