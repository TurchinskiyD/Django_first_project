import calendar
from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    "aries": "Знак зодіаку Овен. March 21 — April 20. Овна потрібно обіймати, коли він не посміхається, цілувати, коли тупить, і годувати, коли в нього істерика.",
    "taurus": "Знак зодіаку Телець. April 21 — May 22. Щастя для Тельця — це багато подорожувати, смачно їсти і бути з коханою людиною",
    "gemini": "Знак зодіаку Близнюки. May 23 — June 21. Якщо Близнюки вирішать зробити когось щасливим, то людину вже ніщо не врятує!",
    "cancer": "Знак зодіаку Рак. June 22 — July 22. Коли терпінню Раків настає межа, тоді починається повне беззаконня.",
    "leo": "Знак зодіаку Лев. July 23 — August 22. Міцний характер Левів, як правило, будується з цегли, яку в нього кидали.",
    "virgo": "Знак зодіаку Діва. August 23 — September 22. Найкраще закінчення суперечки з Дівою — прикинутися мертвим.",
    "libra": "Знак зодіаку Терези. September 23 — October 22. У всіх Терезів є два життя: одне бачать всі ті, хто їх оточує, іншим живуть вони одні.",
    "scorpion": "Знак зодіаку Скорпіон. October 23 — November 21. Скорпіони — це ті люди, яким вкрай необхідно знайти баланс між спокоєм і високим ступенем активності.",
    "sagittarius": "Знак зодіаку Стрілець. November 22 — December 22. 99% Стрільців були народжені для того, щоб основним сенсом їхнього існування так чи інакше стала дорога.",
    "capricorn": "Знак зодіаку Козеріг. December 23 — January 20. Козероги люблять дивних людей.",
    "aquarius": "Знак зодіаку Водолій. January 21 — February 19. Водолії не дивуються чиїмось дивацтвам… Вони і свої-то не завжди пояснити можуть.",
    "pisces": "Знак зодіаку Риби. February 20 — March 20. Добре, що думки Риб ніхто не може читати, а то образ сором’язливих людей полетів би до біса."
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"

    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Було передано невірний порядковий номер знаку зодіаку {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_zodiac_elements(request):
    elements = ['fire', 'air', 'earth', 'water']

    li_elements = ''
    for element in elements:
        redirect_path = reverse('horoscope_name', args=[element])
        li_elements += f"<li><a href='{redirect_path}'>{element.title()}</a></li>"

    response = f"""
    <h3>Zodiac Elements:</h3>
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_zodiac_type(request, type_zodiac):
    elements = {
        'fire': ['aries', 'leo', 'sagittarius'],
        'air': ['gemini', 'libra', 'aquarius'],
        'earth': ['taurus', 'virgo', 'capricorn'],
        'water': ['cancer', 'scorpion', 'pisces']
    }
    type_zodiac_lower = type_zodiac.lower()
    if type_zodiac_lower in elements:
        zodiacs = elements[type_zodiac.lower()]

        li_elements = ''
        for zodiac in zodiacs:
            redirect_path = reverse('horoscope_name', args=[zodiac])
            li_elements += f"<li><a href='{redirect_path}'>{zodiac.title()}</a></li>"

        response = f"""
        <h3>Zodiac Signs ({type_zodiac.title()}):</h3>
        <ul>
            {li_elements}
        </ul>
        """
        return HttpResponse(response)
    elif type_zodiac_lower in zodiac_dict:
        return get_info_about_zodiac(request, type_zodiac_lower)
    else:
        return HttpResponseNotFound(f'Невідомий тип стихії - {type_zodiac}')


def get_info_about_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f'<h3>{description}</h3>')
    else:
        return HttpResponseNotFound(f'Невідомий знак зодіаку - {sign_zodiac}')

zodiac_dict_date = {
    # Знаки зодіаку з місяцями та днями
    "aries": (3, 21, 4, 20),
    "taurus": (4, 21, 5, 20),
    "gemini": (5, 21, 6, 20),
    "cancer": (6, 21, 7, 22),
    "leo": (7, 23, 8, 22),
    "virgo": (8, 23, 9, 22),
    "libra": (9, 23, 10, 22),
    "scorpion": (10, 23, 11, 21),
    "sagittarius": (11, 22, 12, 21),
    "capricorn": (12, 22, 1, 20),
    "aquarius": (1, 21, 2, 19),
    "pisces": (2, 20, 3, 20),
}
def get_info_by_date(request,month, day):
    try:
        month = int(month)
        day = int(day)
    except ValueError:
        return HttpResponseNotFound(f'Невірний формат дати - {month}/{day}')

    if not (1 <= month <= 12):
        return HttpResponseNotFound(f'Невірний номер місяця - {month}.')

    year = datetime.now().year
    _, max_day = calendar.monthrange(year, month)  # max_day = calendar.monthrange(year, month)[1]

    if not (1 <= day <= max_day):
        return HttpResponseNotFound(f'Такого дня - {day} не має в місяці - {month}')


    zodiac_sign = None
    for sign, (start_month, start_day, end_month, end_day) in zodiac_dict_date.items():
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            zodiac_sign = sign
            break

    if zodiac_sign:
        zodiac_info = zodiac_dict.get(zodiac_sign)
        return HttpResponse(f'<h2>Місяць - {month}, день - {day}. Знак зодіаку: {zodiac_sign.title()}.</h2>{zodiac_info}')
    else:
        HttpResponseNotFound(f'Невідома дата - {month}/{day}')