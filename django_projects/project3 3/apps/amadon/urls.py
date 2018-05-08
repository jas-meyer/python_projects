from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^amadon$', views.index), 
 	url(r'^amadon/buy$', views.buy),
 	url(r'^amadon/checkout$', views.checkout),    						
  ]
