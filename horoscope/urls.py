from django.urls import path
from .views import aries, taurus, gemini, cancer, leo, virgo, libra, scorpion, sagittarius, capricorn, aquarius, pisces


urlpatterns = [
    path('aries/', aries),
    path('taurus/', taurus),
    path('gemini/', gemini),
    path('cancer/', cancer),
    path('leo/', leo),
    path('virgo/', virgo),
    path('libra/', libra),
    path('scorpion/', scorpion),
    path('sagittarius/', sagittarius),
    path('capricorn/', capricorn),
    path('aquarius/', aquarius),
    path('pisces/', pisces)
]
