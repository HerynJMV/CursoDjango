"""Platzigram views."""
#Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    
    return HttpResponse('Holiii {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))


def sort_integers(request):
    """Return a JSON response with sorted integers"""
    numbers = map(int, request.GET["numbers"].split(","))

    return JsonResponse({ "numbers" : sorted(
        numbers)},json_dumps_params={'indent': 4})


def say_hi(request, name, age):
    """Returns a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)