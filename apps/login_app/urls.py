from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addsubscriber', views.addsubscriber),
    url(r'^thankyou', views.thankyouPage),
    url(r'^logpage', views.logpage),
    url(r'^login', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard', views.dashboard),
    url(r'^add', views.add),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<id>\d+)$', views.deleteview),
]
