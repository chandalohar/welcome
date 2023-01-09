from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    res=HttpResponse("<html> welcome to lokesh it</html>")
    return res
