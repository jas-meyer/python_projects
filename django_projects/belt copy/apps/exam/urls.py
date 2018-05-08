from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.create), 
    url(r'^process2$', views.login), 
    url(r'^appointments$', views.success), 
    url(r'^appointments/add$', views.success), 
  		    						
  ]