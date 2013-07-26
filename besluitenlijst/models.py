from django.db import models

class Alv(models.Model):
  datum = models.DateField('datum alv')
   
  def __unicode__(self):
    return "Alv van " + self.datum.strftime("%d-%m-%Y")

class Besluit(models.Model):
  class Meta:
    verbose_name_plural = 'Besluiten'

  besluit = models.TextField('Tekst besluit')
  alv = models.ForeignKey(Alv)
  volgnummer = models.PositiveIntegerField()

  def __unicode__(self):
    return self.besluit



# Create your models here.
