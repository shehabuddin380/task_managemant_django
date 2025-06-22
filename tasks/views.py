from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("welccome to the task managment system")
def contact(request):
    return HttpResponse("This is contact page")

def show_task(request):
    return HttpResponse("this is our task page")