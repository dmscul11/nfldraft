from django.conf.urls import url
from . import views


app_name = 'nfldata'
urlpatterns = [
    url(r'^add-nfldata/$', views.add_nfldata),
    url(r'^$', views.index, name='index')
]
