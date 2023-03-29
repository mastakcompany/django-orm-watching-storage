from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.utils import format_duration_output


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = list()

    for visit in visits:
        duration = visit.format_duration(visit.get_duration())
        passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration_output(duration),
            'is_strange': visit.is_visit_long()
        }
        this_passcard_visits.append(passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
