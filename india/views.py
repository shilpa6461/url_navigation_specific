from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def user(request):
    return HttpResponse('User interface')
def raina(request):
    return render(request,'raina.html')