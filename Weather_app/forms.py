from django import forms
from . models import City
from django.core.exceptions import ValidationError

class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data["name"]
        if City.objects.filter(name=name).exists():
            raise ValidationError("Already Exists")
        else:
            return self.cleaned_data["name"]
