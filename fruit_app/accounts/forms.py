
from django import forms

from fruit_app.accounts.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
                   }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'image_url', 'age')
        labels = { 'first_name': 'First Name',
                   'last_name': 'First Name',
                   'image_url': 'Image URL', }
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'Image URl'}),
                   }
