from django import forms
from .models import Product, Category


#   ProductForm extends the built in 'forms.model' form
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #  double underscore string 'all' which includes all the fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        #   List comprehension syntax
        #   It creates a 'for' loop that adds items to a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
