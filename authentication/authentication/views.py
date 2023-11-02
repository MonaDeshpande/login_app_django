from django.http import HttpResponse
from django.shortcuts import render

def signup(request):
    # return HttpResponse("this is signup page")
    return render(request, "signup/signup.html", {})