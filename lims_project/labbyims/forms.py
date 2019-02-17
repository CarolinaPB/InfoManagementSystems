from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class AdvancedSearch(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-12'}))
    CHOICES=[('unit', 'Unit'),
             ('location','Location'),
             ('item_type','Item type'),
             ('finished', 'Finished')
             ]
    advanced_search = forms.ChoiceField(choices=CHOICES)
    advanced_search.widget.attrs.update({'class': 'col-md-4'})
    advanced_search.widget.attrs.update({'name': 'advanced_search'})
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            "search",
            "advanced_search",
            Submit("submit", "Search", css_class="btn")
        )

class BasicSearch(forms.Form):
    search = forms.CharField(label=False)
    search.widget.attrs.update({'placeholder': 'Search'})
    search.widget.attrs.update({'name': 'basic_search'})
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            "search",
            Submit("submit", "Search", css_class="btn")
        )
