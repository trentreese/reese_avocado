from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='form_checks', max_length=100)