from django.contrib import admin
from .models import Tipologia
from .models import Expedient
from .models import Fitxa

# Register your models here.
admin.site.register(Tipologia)
admin.site.register(Fitxa)
admin.site.register(Expedient)
