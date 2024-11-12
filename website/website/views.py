from django.http import HttpResponse
from django.shortcuts import render





# def home(request):
#     return render(request, 'base.html',)

# def upload(request):
#     return render(request, 'upload.html')

# def help(request):
#     return render(request,'help.html')

# def settings(request):
#     return render(request,'settings.html')

# def generate_summary(request):
#     return render(request,'generate_summary.html')

# def login(request):
#     return render(request,'login.html')

def home(request):
    return render(request, 'base.html')  # Main home page or dashboard.

def upload_view(request):
    return render(request, 'upload.html')

def help_view(request):
    return render(request, 'help.html')

def generate_summary_view(request):
    return render(request, 'generate_summary.html')

def settings_view(request):
    return render(request, 'settings.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

