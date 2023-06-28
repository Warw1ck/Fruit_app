from django import forms
from django.forms import TextInput, CharField, URLField

from fruit_app.fruit.models import FruitModel


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Fruit name'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
                   'nutrients': forms.Textarea(attrs={'placeholder': 'Nutrient Info'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'})}
        labels = {'name': 'Name',
                  'image_url': 'Image URL',}


class CreateFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disable'] = 'disable'