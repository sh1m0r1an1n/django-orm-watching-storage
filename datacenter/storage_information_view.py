from django.shortcuts import render
from django.utils import timezone
from datacenter.models import Visit, get_duration, format_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': timezone.localtime(
                visit.entered_at).replace(microsecond=0),
            'duration': format_duration(get_duration(visit)),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
