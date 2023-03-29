from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.utils import format_duration_output


def storage_information_view(request):
    non_closed_visits = list()
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration = visit.format_duration(visit.get_duration())

        not_leaved = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration_output(duration)
        }
        non_closed_visits.append(not_leaved)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
