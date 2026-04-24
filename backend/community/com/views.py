from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def create(request):

    print(request.body)
    data=json.loads(request.body)
    name=data.get("name")
    surname=data.get("surname")
    area=data.get("area")
    party=data.get("party")
    create_person=models.Community(person_name=name,person_surname=surname,person_area=area,person_party=party)
    create_person.save()

    return JsonResponse({
        "data":"the item is created"
    },safe=False)


def get_list(request):
    return HttpResponse("Got the full list")


def delete_one(request):
    return HttpResponse("deleted One thing")

def update_one(request):
    return HttpResponse("updated one item")