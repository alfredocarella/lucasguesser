from datetime import datetime
from dateutil.parser import parse
from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    with open("polls/guesstimates.json") as guess_list:
        guess_by_person = json.load(guess_list)

    with open("polls/template.html", "r") as content_file:
        content = content_file.read()

    person_by_date = {parse(value):key for key, value in guess_by_person.items()}
    dates = sorted(list(person_by_date.keys()))
    best_guess = nearest(dates, datetime.today())
    winner = person_by_date[best_guess]
    response = content.format(winner, get_table(dates, person_by_date, best_guess))
    return HttpResponse(response)


def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def get_table(list_of_keys, dictionary, best_guess):
    table = ""
    for key in list_of_keys:
        name = "<strong>"+dictionary[key]+"</strong>" if key == best_guess else dictionary[key]
        date = "<strong>"+str(key)+"</strong>" if key == best_guess else key
        table += """
        <tr>
        <td>{0}</td>
        <td>{1}</td>
        </tr>""".format(name, date)
    return table

