from django.conf.urls import patterns, url

from besluitenlijst import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^alv/(?P<pk>\d+)/$', views.AlvView.as_view(), name='alv'),
    url(r'^tex$', views.tex),
    )
