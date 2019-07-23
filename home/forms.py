from django import forms

class form_r(forms.Form):
    CHOICES = [('1', 'Currently Reading'), ('2', 'Read')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)