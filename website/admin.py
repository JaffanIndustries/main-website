from django.contrib import admin
from .models import about, services, update, product
# Register your models here.
admin.site.register(about)
admin.site.register(services)
admin.site.register(update)
admin.site.register(product)