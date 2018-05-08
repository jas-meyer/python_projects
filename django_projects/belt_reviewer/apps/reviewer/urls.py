from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.create), 
    url(r'^process2$', views.login), 
    url(r'^process3$', views.process3),
    url(r'^process4/(?P<id>\d+)$', views.process4),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^books$', views.success), 
    url(r'^books/add$', views.add),
    url(r'^books/(?P<id>\d+)$', views.book),
    url(r'^users/(?P<id>\d+)$', views.user),
    url(r'^logout$', views.logout),
  		    						
  ]