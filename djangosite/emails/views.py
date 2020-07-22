from django.shortcuts import render
from django.http import HttpResponse


def emails(request):
    return HttpResponse('Done!')