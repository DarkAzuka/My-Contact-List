from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio, Ocupacion


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'numero_ext': TextInput(attrs={'type': 'number'}),
            'numero_int': TextInput(attrs={'type': 'number'})
        }


class OcupacionForm(ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
