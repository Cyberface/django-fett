from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^simple_chart/$', views.simple_chart, name='simple_chart'),
    url(r'^simple_chart_same_axis/$', views.simple_chart_same_axis, name='simple_chart_same_axis'),
]
