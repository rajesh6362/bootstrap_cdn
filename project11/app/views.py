from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')

def submit(request):
    return render(request,'submit.html')
