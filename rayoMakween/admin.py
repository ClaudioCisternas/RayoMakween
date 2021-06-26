from django.contrib import admin
from .models import Contacto, TipoTrabajo, Trabajo, Galeria, Contacto

# Register your models here.
admin.site.register(TipoTrabajo)
admin.site.register(Trabajo)
admin.site.register(Galeria)
admin.site.register(Contacto)