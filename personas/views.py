from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def Menu(request):
    no_personas = Persona.objects.count()
    info_persona = Persona.objects.order_by('dni')
    # info_persona = Persona.objects.all()
    return render(request, 'principal_menu.html', {'no_personas': no_personas, 'info_persona': info_persona})


def detallesPersona(request, nombres):
    persona_detalle = Persona.objects.get(pk=nombres)
    return render(request, 'detalles_persona.html',
                  {'persona_detalle': persona_detalle})


# ersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        form_persona = PersonaForm(request.POST)
        if form_persona.is_valid():
            form_persona.save()
            return redirect('index')
    else:
        form_persona = PersonaForm()

    return render(request, 'nueva_persona.html', {'form_persona': form_persona})


def editarPersona(request, nombres):
    person = get_object_or_404(Persona, pk=nombres)
    if request.method == 'POST':
        form_persona = PersonaForm(request.POST, instance=person)
        if form_persona.is_valid():
            form_persona.save()
            return redirect('index')
    else:
        form_persona = PersonaForm(instance=person)

    return render(request, 'editar_persona.html', {'form_persona': form_persona})


def eliminarPersona(request, nombres):
    person = get_object_or_404(Persona, pk=nombres)
    if person:
        person.delete()
    return redirect('index')
