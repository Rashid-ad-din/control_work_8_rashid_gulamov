from django import forms
from django.forms import Textarea, TextInput
from django.forms.widgets import Select

from webapp.models import Product


class ProductForm(forms.ModelForm):
    error_css_class = 'error'
    label_css_class = 'label'

    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'image')
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control w-75",
            }),
            'category': Select(attrs={
                'class': "form-control w-75",
            }),
            'description': Textarea(attrs={
                'class': "form-control w-75"
            })
        }
