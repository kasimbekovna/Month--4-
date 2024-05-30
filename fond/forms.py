from django import forms
from . import models


GENDER = (("Male", "Male"), ("Female", "Female"))


class SocFondUserForm(forms.ModelForm):
    class Meta:
        model = models.SocFondUser
        fields = ["username", "pin_number", "password", "age", "gender", "stag"]
