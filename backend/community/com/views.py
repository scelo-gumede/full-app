from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def create(request):
    return HttpResponse("that the creation")


def get_list(request):
    return HttpResponse("Got the full list")


def delete_one(request):
    return HttpResponse("deleted One thing")

def update_one(request):
    return HttpResponse("updated one item")