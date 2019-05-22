from django import forms
from .models import Hotel
class Reviews(forms.ModelForm):
      class Meta:
        model = Hotel
        fields = ['rating', 'review']

