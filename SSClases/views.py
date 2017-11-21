from Clases.models import Clases
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView

from Clases.forms import ClassForm


#administrador
def class_lists(request):
    all_class = Clases.objects.all()
    context ={
        'all_class': all_class
        }
    return render(request, 'SSClases/clases_list.html',context)

def class_delete(request, pk):
    clase = Clases.objects.filter(pk=pk)
    clase.delete()
    return HttpResponseRedirect(reverse('SSClases:class_lists'))


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
    return render(request, 'SSClases/clases_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'SSClases/clases_form.html', context)

class class_update(UpdateView):
    model = Clases
    fields = [
        'nombre',
        'descripcion',
        'horario',
        'requisitos',
        'estudiantes',
    ]
    template_name = 'SSClases/clases_edit_form.html'

    success_url = reverse_lazy('SSClases:class_lists')

#estudiante
#def class student_class_lists

