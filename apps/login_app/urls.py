from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^logpage', views.logpage),
    url(r'^login', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard', views.dashboard),
]
