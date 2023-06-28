from django.urls import path
from .views import get_info_about_zodiac, get_info_about_zodiac_by_number, index

urlpatterns = [
    path('', index),
    path('<int:sign_zodiac>/', get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>/', get_info_about_zodiac, name='horoscope_name')

]
