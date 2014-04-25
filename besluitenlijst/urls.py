from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from besluitenlijst import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^alv/(?P<pk>\d+)/$', login_required(views.AlvView.as_view()), name='alv'),
    url(r'^tex$', views.tex),
    url(r'^accounts/login/*', TemplateView.as_view(template_name='login.html'))
)
