# Create your views here.

from django.http import HttpResponse, Http404
from django.views import generic
from django.shortcuts import render, get_object_or_404
from besluitenlijst.models import Alv

class IndexView(generic.ListView):
  template_name = 'besluitenlijst/index.html'
  context_object_name = 'alvlijst'

  def get_queryset(self):
    """Return the list with ALVs"""
    return Alv.objects.order_by('-datum')

class AlvView(generic.DetailView):
  template_name = 'besluitenlijst/alv.html'
  model = Alv


