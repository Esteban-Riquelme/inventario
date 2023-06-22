from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'login.html')


def inicio(request):
    return render(request,'inicio.html')

def busqueda(request):
    return render(request,'busqueda.html')


def tabla(a):
    pass