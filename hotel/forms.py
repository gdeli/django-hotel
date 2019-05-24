from django import forms
from .models import Hotel,reviewer
class Reviews(forms.ModelForm):
      class Meta:
        model = reviewer
        fields = ['rating', 'review',]

