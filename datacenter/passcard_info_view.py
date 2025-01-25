from datacenter.models import Passcard, get_duration, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    # Программируем здесь

    # 1. Получить пропуск по passcode QuerySet.get()
    # passcard = Passcard.objects.get(passcode=passcode)

    # 1.1 Получаем объект Passcard по passcode или возвращаем ошибку 404, если не найден
    passcard = get_object_or_404(Passcard, passcode=passcode)

    # 2. Получить все визиты по пропуску QuerySet.filter()
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append({
            'entered_at': timezone.localtime(visit.entered_at).replace(microsecond=0),
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
