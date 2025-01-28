from django.db import models
from django.utils import timezone
from datetime import timedelta


def get_duration(visit):
    entered_at_moscow = timezone.localtime(
        visit.entered_at).replace(microsecond=0)

    leaved_at_moscow = timezone.localtime(
        visit.leaved_at if visit.leaved_at else timezone.now()
    ).replace(microsecond=0)

    return leaved_at_moscow - entered_at_moscow


def format_duration(duration):
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return f'{hours}ч {minutes:02d}мин'


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)


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
