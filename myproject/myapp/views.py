

# Create your views here.



from django.shortcuts import render


def home(request):
    return render(request,"index.html")

def index(request):
    return render(request,'lists.html')

def login_url(request):
    return render(request,'login.html')
    