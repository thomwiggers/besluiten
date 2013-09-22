from django.db import models

class Alv(models.Model):
  datum = models.DateField('datum alv')
   
  def __unicode__(self):
    return "Algemene Ledenvergadering van " + self.datum.strftime("%d-%m-%Y")

class Besluit(models.Model):
  class Meta:
    verbose_name_plural = 'Besluiten'

  besluit = models.TextField('Tekst besluit')
  alv = models.ForeignKey(Alv)
  volgnummer = models.PositiveIntegerField()
  valid = models.BooleanField('Besluit nog geldig', default = True)

  def __unicode__(self):
    return self.besluit

  class Meta:
    ordering = ['volgnummer']

class Contributors(models.Model):
  contributor = models.TextField('Bijdrager')

  def __unicode__(self):
    return self.contributor

  class Meta:
    ordering = ['contributor']



# Create your models here.
