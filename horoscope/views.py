from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def aries(request):
    return HttpResponse("Знак зодіаку Овен. March 21 — April 20")


def taurus(request):
    return HttpResponse("Знак зодіаку Телець. April 21 — May 22")


def gemini(request):
    return HttpResponse("Знак зодіаку Близнюки. May 23 — June 21")


def cancer(request):
    return HttpResponse("Знак зодіаку Рак. June 22 — July 22")


def leo(request):
    return HttpResponse("Знак зодіаку Лев. July 23 — August 22")


def virgo(request):
    return HttpResponse("Знак зодіаку Діва. August 23 — September 22")


def libra(request):
    return HttpResponse("Знак зодіаку Терези. September 23 — October 22")


def scorpion(request):
    return HttpResponse("Знак зодіаку Скорпіон. October 23 — November 21")


def sagittarius(request):
    return HttpResponse("Знак зодіаку Стрілець. November 22 — December 22")


def capricorn(request):
    return HttpResponse("Знак зодіаку Козоріг. December 23 — January 20")


def aquarius(request):
    return HttpResponse("Знак зодіаку Водолій. January 21 — February 19")


def pisces(request):
    return HttpResponse("Знак зодіаку Риби. February 20 — March 20")
