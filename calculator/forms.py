from django import forms
from .models import Breeds


class BreedForm(forms.ModelForm):

    class Meta:
        model = Breeds
        #  double underscore string 'all' which includes all the fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        breeds = Breeds.objects.all()
        #   List comprehension syntax
        #   It creates a 'for' loop that adds items to a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in breeds]

        self.fields['breed'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
