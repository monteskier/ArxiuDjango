from django.contrib import admin
from .models import Tipologia
from .models import Expedient
from .models import Fitxa

# Register your models here.
admin.site.register(Tipologia)
admin.site.register(Fitxa)
admin.site.register(Expedient)

admin.site.site_title = 'Arxiu SVC'
admin.site.site_header = 'Administracio del Arxiu Ajuntament de Sant Vicenç de Castellet'
