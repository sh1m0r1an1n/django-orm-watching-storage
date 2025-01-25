from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.models import get_duration, format_duration


def storage_information_view(request):
    # Программируем здесь

    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
