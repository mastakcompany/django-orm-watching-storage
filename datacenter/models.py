import datetime

from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if not self.leaved_at:
            duration_time = localtime() - localtime(self.entered_at)
            return duration_time.total_seconds()
        duration_time = self.leaved_at - self.entered_at
        return duration_time.total_seconds()

    @staticmethod
    def format_duration(duration):
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        return hours, minutes, seconds

    def is_visit_long(self, minutes=10):
        if not self.leaved_at:
            entered_minutes = self.get_duration() // 60
            return (entered_minutes - minutes) < 0
        return datetime.timedelta(seconds=self.get_duration()) > datetime.timedelta(minutes=minutes)
