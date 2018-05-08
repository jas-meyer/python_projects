from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.process), 
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy), 
    url(r'^delete/(?P<id>\d+)$', views.delete), 
     
  		    						
  ]