from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"

        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
        }