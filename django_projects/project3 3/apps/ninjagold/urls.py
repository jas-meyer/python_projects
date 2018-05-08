from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^ninjagold$', views.index), 
  	url(r'^ninjagold/process$', views.process),
  	url(r'^ninjagold/reset$', views.clear),
  ]
