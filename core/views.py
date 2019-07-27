from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home page view
def home(request):

    response = HttpResponse('Hello , Ahmad')

    return response

    