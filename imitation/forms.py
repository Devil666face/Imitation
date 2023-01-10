from django import forms
from imitation.models import (
    Incident,
    Category,
    ExampleIncident,
)
from django.core.exceptions import ValidationError


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.attrs.get('class') not in ['form-check-input']:
                self.fields[field].widget.attrs['class'] = 'form-control'


class IncidentCreateForm(BootstrapForm):
    class Meta:
        model = Incident
        fields = [
            'title',
            'category',
            'legal',
            'ip',
            'hostname',
        ]
        widgets = {
            'category':forms.Select(attrs={"class":""}),
        }

        
class CategoryCreateForm(BootstrapForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]

        
class ExampleIncidentCreateForm(BootstrapForm):
    class Meta:
        model = ExampleIncident
        fields = [
            'title',
            'category',
            'legal',
        ]
