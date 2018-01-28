from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    with open("polls/guesstimates.json") as guess_list:
        guesstimates = json.load(guess_list)

    response = "Hello, world. You are at the polls index now.\n"
    for key in guesstimates:
        response += "{0} guessed {1}\n".format(key, guesstimates[key])
    return HttpResponse(response)

