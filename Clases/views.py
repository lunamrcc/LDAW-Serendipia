from .models import Clases, Asistencia
from Estudiantes.models import Estudiantes

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView

from .forms import ClassForm


def assistance_lists(request):
    context = {}
    return render(request, 'Clases/asistencia_list.html', context)


#administrador
def class_lists(request):
    all_class = Clases.objects.all()
    context ={
        'all_class': all_class
        }
    return render(request, 'Clases/clases_list.html',context)

def class_delete(request, pk):
    clase = Clases.objects.filter(pk=pk)
    clase.delete()
    return HttpResponseRedirect(reverse('Clases:class_lists'))


def class_create(request):
    context = {}
    NewClassForm = ClassForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        NewClassForm = ClassForm(request.POST)
        ClassValid = NewClassForm.is_valid()

        # check whether it's valid
        if ClassValid:
            Class = NewClassForm.save(commit=False)
            Class.Activo = True
            ID = Clases.objects.count() + 1
            Class.pk = ID
            Class.save()
            return class_lists(request)

    context = {
        'NewClassForm': NewClassForm
    }
    return render(request, 'Clases/clases_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'Clases/clases_form.html', context)

class class_update(UpdateView):
    model = Clases
    fields = [
        'nombre',
        'descripcion',
        'horario',
        'requisitos',
        'estudiantes',
    ]
    template_name = 'Clases/clases_edit_form.html'

    success_url = reverse_lazy('Clases:class_lists')



#estudiante

def student_class_lists(request, pk):
    all_class = Clases.objects.filter(estudiantes=(Estudiantes.objects.get(EstudianteID=pk)))
    estudiante = Estudiantes.objects.get(EstudianteID=pk)
    context = {
        'Estudiante': estudiante,
        'all_class': all_class
    }
    return render(request, 'Clases/student_clases_list.html', context)

def student_assistance(request, pk):
    # estudiante = Estudiantes.objects.get(EstudianteID=pk)
    # context = {
    #     'Estudiante': estudiante,
    # }

    all_class = Clases.objects.filter(estudiantes=(Estudiantes.objects.get(EstudianteID=pk)))
    estudiante = Estudiantes.objects.get(EstudianteID=pk)
    context = {
        'Estudiante': estudiante,
        'all_class': all_class
    }
    return render(request, 'Clases/student_assistance.html', context)
