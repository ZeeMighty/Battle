from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from mains.models import event
from mains.models import heroe

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<event_id>[0-9]+)/$', views.EventView, name = 'EventView'),
#    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = event, template_name = "mains/events.html")),
    url(r'^(?P<heroe_id>[0-9]+)/heroe/$', views.hero, name='hero'),
    url(r'dates/', views.Dates, name = 'dates'),
]
