# Create your views here.

from django.http import HttpResponse, Http404
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from besluitenlijst.models import Alv, Contributors
from version import version
import datetime

class IndexView(generic.ListView):
  template_name = 'besluitenlijst/index.html'
  context_object_name = 'alvlijst'

  def get_queryset(self):
    """Return the list with ALVs"""
    return Alv.objects.order_by('-datum')

class AlvView(generic.DetailView):
  template_name = 'besluitenlijst/alv.html'
  model = Alv

def tex(request):
  alvs = Alv.objects.order_by('-datum')
  datum = datetime.datetime.now().strftime("%d -- %m -- %Y, %H:%M uur")
  response = HttpResponse(content_type='text/tex')
  response['Content-Disposition'] = 'attachment; filename="besluitenlijst.tex"'



  response.write(render_to_string('besluitenlijst/besluitenlijst.pytex', {'alvs': alvs, 
    'datum' : datum,
    'version': version,
    'contributors': Contributors.objects.all() } ) )

  return response


