from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = list()
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        name = visit.passcard
        entered_time = visit.entered_at
        duration = visit.format_duration(visit.get_duration())

        not_leaved = {
            'who_entered': name,
            'entered_at': entered_time,
            'duration': "{:.0f} ч {:.0f} мин".format(*duration[:2])
        }
        non_closed_visits.append(not_leaved)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
