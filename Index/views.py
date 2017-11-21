from django.shortcuts import render

# Create your views here.
def Index(request):
	context = {}
	return render(request, 'Index/dashboard_admin.html', context)

def Index_alumno(request):
	context = {}
	return render(request, 'Index/dashboard_alumno.html', context)
def Index_ssadmin(request):
	context = {}
	return render(request, 'Index/dashboard_ssadmin.html', context)