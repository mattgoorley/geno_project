from django import forms
from drugs.models import Entities, Drugs

class EntitiesForm(forms.ModelForm):
    class Meta:
        model = Entities
        fields = [
            'name',
            'entity_type',
        ]

class DrugsForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = [
            'name_main',
            'condition_name',
            'admin_route',

        ]


