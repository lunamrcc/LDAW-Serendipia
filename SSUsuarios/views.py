from django.shortcuts import render
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy

from Usuarios.models import Usuarios
from Estudiantes.models import Estudiantes

from Usuarios.forms import UsuariosForm, LoginForm

# Create your views here.

def login(request):
    context = {}
    NewLoginForm = LoginForm()

    #Checar POST
    if request.method == 'POST':
        NewLoginForm = LoginForm(request.POST)
        UserValid = NewLoginForm.is_valid()

        #Checar que la forma sea valida
        if UserValid:
            Usu = NewLoginForm.save(commit=False)

            #Checar que el usuario sea Administrador
            emailValid = Usuarios.objects.filter(Email=Usu.Email, Passwd=Usu.Passwd)
            alumnoValid = Estudiantes.objects.filter(Correo=Usu.Email, Passwd=Usu.Passwd)
            if emailValid.count() > 0:
                return render(request, 'Index/dashboard_admin.html', context)
            elif alumnoValid.count() > 0:
                context = {
                    'Estudiante': alumnoValid
                }
                return render(request, 'Index/dashboard_alumno.html', context)

        context = {
            'NewLoginForm': NewLoginForm
        }
        return render(request, 'Index/login.html', context)

    context = {
        'NewLoginForm': NewLoginForm
    }
    return render(request, 'Index/login.html', context)

def user_lists(request):
    all_users = Usuarios.objects.all()
    context ={
        'all_users': all_users
        }
    return render(request, 'SSUsuarios/usuarios_list.html',context)


def user_create(request):
    context = {}
    NewUsuariosForm = UsuariosForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        NewUsuariosForm = UsuariosForm(request.POST)
        UserValid = NewUsuariosForm.is_valid()

        # check whether it's valid
        if UserValid:
            Usu = NewUsuariosForm.save(commit=False)
            Usu.Activo = True
            ID = Usuarios.objects.count() + 1
            Usu.Usuarioid = ID
            Usu.save()
            return user_lists(request)

    context = {
        'NewUsuariosForm': NewUsuariosForm
    }
    return render(request, 'SSUsuarios/usuarios_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'SSUsuarios/usuarios_form.html', context)

class user_update(UpdateView):
    model = Usuarios
    fields = [
        'Nombre',
        'Apaterno',
        'Amaterno',
        'Telefono',
        'Email',
        'Passwd'
    ]
    template_name = 'SSUsuarios/user_edit_form.html'

    success_url = reverse_lazy('SSUsuarios:user_lists')

def user_delete(request, pk):
    user = Usuarios.objects.filter(pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('SSUsuarios:user_lists'))

def user_change_status(request, pk):
    user = Usuarios.objects.get(pk=pk)
    if user.Activo:
        user.Activo = False
        user.save()
    else:
        user.Activo = True
        user.save()
    return HttpResponseRedirect(reverse('SSUsuarios:user_lists'))


