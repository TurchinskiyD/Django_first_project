from django.urls import path, register_converter
from .views import get_info_about_zodiac, get_info_about_zodiac_by_number, index, get_info_about_zodiac_type, \
    get_zodiac_elements, get_info_by_date

urlpatterns = [
    path('', index),
    path('<int:month>/<int:day>/', get_info_by_date),
    path('type/<str:type_zodiac>/', get_info_about_zodiac_type, name='horoscope_type_zodiac'),
    path('type/', get_zodiac_elements, name='horoscope_type_elements'),
    path('<int:sign_zodiac>/', get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>/', get_info_about_zodiac, name='horoscope_name')
]
