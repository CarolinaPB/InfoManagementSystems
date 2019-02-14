from django import forms

class AdvancedSearch(forms.Form):
    CHOICES=[('unit', 'Unit'),
             ('location','Location'),
             ('item_type','Item type'),
             ('finished', 'Finished')
             ]
    Advanced_search = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
