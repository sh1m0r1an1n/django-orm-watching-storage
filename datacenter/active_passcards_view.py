from datacenter.models import Passcard, Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь


    # 0. Изначальный код
    # all_passcards = Passcard.objects.all()
    # context = {
    #     'active_passcards': all_passcards,  # люди с активными пропусками
    # }
    # return render(request, 'active_passcards.html', context)


    # 1. Только активные карточки
    all_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
