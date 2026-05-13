from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class MagicLinkForm(forms.Form):
    email = forms.EmailField(label='O teu email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'exemplo@email.com'
    }))
