from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
  	url(r'^process$', views.process),
  	url(r'^back$', views.back),
  	url(r'^result$', views.result)


  	#url(r'^result$', views.result)
  ]