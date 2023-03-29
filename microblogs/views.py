from django.shortcuts import render
# from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.
def home(request):
    # response = HttpResponse("Welcome to clucker!")
    return render(request, 'home.html')

def sign_up(request):
    # response = HttpResponse("Welcome to clucker!")
    form = SignUpForm()
    return render(request, 'sign_up.html',  {'form': form})
