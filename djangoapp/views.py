from os import XATTR_SIZE_MAX
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def myfunctioncall(request):
    return HttpResponse('Hello World')

def myaboutcall(request):
    return HttpResponse('About Response')

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydictionary = {
        'name' : name, 
        'age'  : age,
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request, 'index.html')


def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    vari = 'Hello World'
    greeting = 'Hey, How are you ?'
    fruits = ['Apple', 'Mango', 'bnana']
    num1, num2 = 3, 4
    ans = num1 > num2

    mydictionary = {
        'vari' : vari,
        'msg' : greeting,
        'myfruit' : fruits,
        'num1' : num1,
        'num2' : num2,
        'ans' : ans,
    }
    return render(request, 'third.html' , context=mydictionary)

def myimagepage(request):
    return render(request, 'image.html')