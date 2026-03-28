from django import forms

from .models import ChallengeReport


class ChallengeReportForm(forms.ModelForm):
    class Meta:
        model = ChallengeReport
        fields = ["category", "description"]
        widgets = {
            "category": forms.Select(),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea",
                    "rows": 3,
                    "placeholder": "Describe the problem briefly.",
                }
            ),
        }
        labels = {
            "category": "What kind of issue is it?",
            "description": "Details",
        }
