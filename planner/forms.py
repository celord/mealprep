from django import forms
from django.forms import ModelForm

from .models import Plan


class DateInput(forms.DateInput):
    input_type = "date"


class AddPlanForm(ModelForm):
    class Meta:
        model = Plan
        # fields = fields = '__all__'
        fields = [
            "date",
            "meal",
            "mealtype",
            "photo",
        ]
        widgets = {
            "date": DateInput(),
            # 'comments': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
