from django.shortcuts import render
from .models import about, services, update, product
# Create your views here.
def home(request):
	context = dict()
	context['news'] = about.objects.getall()
	context['products'] = product.objects.getall()
	context['about'] = product.objects.getall()
	context['services'] = product.objects.getall()

	return render(request, template_name="main.html", context=context)