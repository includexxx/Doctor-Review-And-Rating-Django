from django import forms

from .models import Rating


class RatingForm(forms.ModelForm):
    profile_id = forms.IntegerField(widget = forms.HiddenInput(), required = True)
    class Meta:
        model = Rating
        fields = ['rating', 'comment', 'profile_id']

    