from django import forms

from hotel.models import Person, Hotel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    pass


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'pesel', 'sex']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or isinstance(field.widget, forms.NumberInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-select'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['room', 'max_persons']
        widgets = {
            'room': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     Field('room', style="padding-left: 20px;"),
        # )


class RoomFormCreate(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['max_persons']

    def __init__(self, *args, **kwargs):
        super(RoomFormCreate, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'