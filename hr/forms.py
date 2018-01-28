from django import forms
from .models import Person, City

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = kwargs.get('data')
        if data is not None:
            cities = City.objects.filter(country_id=data.get('country'))
        elif self.instance is not None:
            cities = City.objects.filter(country_id=self.instance.country_id)
        else:
            cities = City.objects.none()
        self.fields['city'].queryset = cities
