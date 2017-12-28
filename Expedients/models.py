from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Tipologia(models.Model):
    codi = models.CharField(default=0, max_length=20);
    concepte = models.CharField(max_length=200);
    data_creacio = models.DateTimeField(auto_now=True);
    data_pub = models.DateTimeField('data de publicacio');

    def __str__(self):
        return self.concepte;

class Fitxa(models.Model):
    codi = models.CharField(default = 0, max_length = 100);
    tipus = models.ForeignKey(Tipologia, related_name='tipologia', on_delete=models.CASCADE);
    data_pub = models.DateTimeField('data de publicacio');
    TAD = models.CharField(max_length=200,null=True);
    ubicacio = models.CharField(max_length=200);
    detall = models.TextField(max_length=2000, null=True);
    def __str__(self):
        return str(self.codi);

class Expedient(models.Model):
    numexp = models.CharField(max_length=50);
    observacions = models.CharField(max_length=200, null=True);
    fitxa = models.ForeignKey(Fitxa, related_name='fitxa' ,on_delete=models.CASCADE);
    PRESTEC_CHOICES = (
        ('Prestat', 'Prestat'),
        ('Disponible', 'Disponible'),
    )
    estat = models.CharField(max_length = 15, choices = PRESTEC_CHOICES, default = 'Disponible');

    def __str__(self):              # __unicode__ on Python 2
        return self.numexp;
