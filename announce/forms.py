from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Announce


class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ['title',
                  'description',
                  'image',
                  'appart_type',
                  'space'
        ]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save announce'))

