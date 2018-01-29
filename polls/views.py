from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    with open("polls/guesstimates.json") as guess_list:
        guesstimates = json.load(guess_list)

    with open("polls/template.html", "r") as content_file:
        content = content_file.read()
    response = content
    # for key in guesstimates:
    #     response += "{0} guessed {1}\n".format(key, guesstimates[key])
    return HttpResponse(response)

