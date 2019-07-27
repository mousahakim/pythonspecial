from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    response = HttpResponse('Hello , Ahmad')

    return response


# Changes made by Matiullah

def home(request):

    response = HttpResponse('Hello , Ustad')

    return response

  