# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div, Fieldset, HTML

from .models import DoctorProfile


class DoctorProfileForm(forms.ModelForm):
    
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super(DoctorProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-md-8 mb-0'),
                Column('image', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            )
        )
      
  