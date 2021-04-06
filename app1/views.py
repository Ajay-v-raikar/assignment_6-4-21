from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return render(request,'sample.html')

def display(request,data):
    return HttpResponse(f'<h1>The Recieved data is {data}</h1>')


def addition(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(f'<h1>The Sum of {num1} and {num2} is {num1+num2}</h1>')

def factorial(request,num):
    result=1
    for i in range(2,int(num)+1):
        result*=i
    return HttpResponse(f'<h1>The Factorial of {num} is {result}</h1>')

def operation(request,data):
    return HttpResponse(f'<h1>Answer for ({data}) is {eval(data)}.</h1>')