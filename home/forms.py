from django import forms

class form_r(forms.Form):
    form_r = forms.CharField(label='form_radios', max_length=100)