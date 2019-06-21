from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reggy', views.reggy),
    url(r'^success', views.success),
    url(r'^logout', views.logout),
    url(r'^login', views.login),

]