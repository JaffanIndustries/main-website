from django.shortcuts import render
from .models import about, services, update, product
# Create your views here.
def home(request):
	context = dict()
	context['news'] = update.objects.all()
	context['products'] = product.objects.all()
	context['about'] = about.objects.all()
	context['services'] = product.objects.all()
	return render(request, template_name="main.html", context=context)