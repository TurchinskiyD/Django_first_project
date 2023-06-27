from django.urls import path
from .views import get_info_about_zodiac

urlpatterns = [
    path('<sign_zodiac>/', get_info_about_zodiac)
    # path('aries/', aries),
    # path('taurus/', taurus),
    # path('gemini/', gemini),
    # path('cancer/', cancer),
    # path('leo/', leo),
    # path('virgo/', virgo),
    # path('libra/', libra),
    # path('scorpion/', scorpion),
    # path('sagittarius/', sagittarius),
    # path('capricorn/', capricorn),
    # path('aquarius/', aquarius),
    # path('pisces/', pisces)
]
