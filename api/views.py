from imitation.models import (
    Incident,
    Category,
)
from imitation.mixin import (
    IncidentMixin,
)
from django.views.generic import (
    TemplateView,
)


class APICreateIncidentView(IncidentMixin, TemplateView):
    '''/api/incident/create
        &title=
        &category=
        &legal=YES/NONE/NO
        &ip=192.168.0.101
        &hostname=ARM-007'''
    def get(self, request, *args, **kwargs):
        self.title = request.GET.get(
            'title',
            'Неизвестный инцидент'
        )
        self.category = request.GET.get(
            'category',
            None
        )
        self.legal = request.GET.get(
            'legal',
            'NONE'
        )
        self.ip = request.GET.get(
            'ip',
            '0.0.0.0'
        )
        self.hostname = request.GET.get(
            'hostname',
            'ARM'
        )
        if (not Category.objects.filter(title=self.category).exists()) and (self.category!=None):
            Category.objects.create(title=self.category)
            self.category = Category.objects.get(title=self.category)
        elif self.category!=None:
            self.category = Category.objects.get(title=self.category)
            
        Incident.objects.create(
            title=self.title,
            category=self.category,
            legal=self.legal,
            ip=self.ip,
            hostname=self.hostname).save()
        return super().get(request, *args, **kwargs)
