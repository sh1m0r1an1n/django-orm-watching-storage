from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.models import Visit, Passcard, get_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append({
            'entered_at': timezone.localtime(
                visit.entered_at).replace(microsecond=0),
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
