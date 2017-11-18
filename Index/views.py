from django.shortcuts import render

# Create your views here.
def Index(request):
	context = {}
	return render(request, 'Index/dashboard_admin.html', context)

def Index_alumno(request):
	context = {}
	return render(request, 'Index/dashboard_alumno.html', context)

def Index_SSAdmin(request):
	context = {}
	return render(request, 'Index/dashboard_SSAdmin.html', context)