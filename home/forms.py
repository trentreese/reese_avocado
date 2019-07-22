from django import forms

class form_r(forms.ModelForm):
    form_r = forms.CharField(label='form_radios', max_length=100)