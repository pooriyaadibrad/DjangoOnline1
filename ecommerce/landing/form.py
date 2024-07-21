from django import forms
from . import models

class LandingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)
        for item in LandingForm.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = models.message
        fields = '__all__'