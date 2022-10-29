from django import forms
from django.forms import Textarea
from django.forms.widgets import NumberInput

from webapp.models import Review


class ReviewForm(forms.ModelForm):
    error_css_class = 'error'
    label_css_class = 'label'

    class Meta:
        model = Review
        fields = ('description', 'rating')
        widgets = {

            'description': Textarea(attrs={
                'class': "form-control w-75",
                'value': '{{ project.date_start }}'
            }),
            'rating': NumberInput(attrs={
                'class': "form-control w-75",
                'value': '{{ project.date_start }}'
            })
        }
