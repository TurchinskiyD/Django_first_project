
from django.http import HttpResponse, HttpResponseNotFound


def get_info_about_zodiac(request, sign_zodiac):
    if sign_zodiac == "aries":
        return HttpResponse("Знак зодіаку Овен. March 21 — April 20. Овна потрібно обіймати, коли він не посміхається, цілувати, коли тупить, і годувати, коли в нього істерика.")
    elif sign_zodiac == "taurus":
        return HttpResponse("Знак зодіаку Телець. April 21 — May 22. Щастя для Тельця — це багато подорожувати, смачно їсти і бути з коханою людиною")
    elif sign_zodiac == "gemini":
        return HttpResponse("Знак зодіаку Близнюки. May 23 — June 21. Якщо Близнюки вирішать зробити когось щасливим, то людину вже ніщо не врятує!")
    elif sign_zodiac == "cancer":
        return HttpResponse("Знак зодіаку Рак. June 22 — July 22. Коли терпінню Раків настає межа, тоді починається повне беззаконня.")
    else:
        return HttpResponseNotFound(f"Невідомий знак зодіаку - {sign_zodiac}")
#
#
# def leo(request):
#     return HttpResponse("Знак зодіаку Лев. July 23 — August 22")
#
#
# def virgo(request):
#     return HttpResponse("Знак зодіаку Діва. August 23 — September 22")
#
#
# def libra(request):
#     return HttpResponse("Знак зодіаку Терези. September 23 — October 22")
#
#
# def scorpion(request):
#     return HttpResponse("Знак зодіаку Скорпіон. October 23 — November 21")
#
#
# def sagittarius(request):
#     return HttpResponse("Знак зодіаку Стрілець. November 22 — December 22")
#
#
# def capricorn(request):
#     return HttpResponse("Знак зодіаку Козоріг. December 23 — January 20")
#
#
# def aquarius(request):
#     return HttpResponse("Знак зодіаку Водолій. January 21 — February 19")
#
#
# def pisces(request):
#     return HttpResponse("Знак зодіаку Риби. February 20 — March 20")
