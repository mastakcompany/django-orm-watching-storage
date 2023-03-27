from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = list()

    for visit in visits:
        visits_date = visit.entered_at
        duration = visit.format_duration(visit.get_duration())
        passcard_visit = {
            'entered_at': visits_date,
            'duration': '{:.0f}:{:0>2.0f}:{:0>2.0f}'.format(*duration),
            'is_strange': visit.is_visit_long()
        }
        this_passcard_visits.append(passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
