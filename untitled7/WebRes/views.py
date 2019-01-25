from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from WebRes.models import Module
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import re


def index(request):
    return render_to_response("Main_page.html", {"not_logined": not request.user.is_authenticated })
# Create your views here.

def test1(request):
    tmp = ' '
    for x in Module.objects.all():
        tmp = tmp + x.name + " "
    return HttpResponse(tmp)


def test2(request):
    return render_to_response("index.html", {}),


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return HttpResponse("error")
    else:
        login(request, user)
        return HttpResponseRedirect('/main_page')


def auth_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/main_page")
    else:
        return HttpResponse("Ты не залогинен")


def test3(request):
        return render_to_response("test_inheritance.html", {"not_logined": not request.user.is_authenticated})


def registration(request):
    if re.match("(@mail|@gmail)$", request.POST['email']) is None:
        return HttpResponse("Неверный email")
    else:
        email = request.POST['email']

    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=email
    )
    user.save()
    login(request, user)
    return HttpResponseRedirect('/main_page', )