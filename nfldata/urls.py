from django.conf.urls import url
from . import views


app_name = 'nfldata'
urlpatterns = [
    url(r'^add-nfldata/$', views.add_nfldata),
    url(r'^begin-draft/$', views.begin_draft),
    url(r'^$', views.index, name='index')
]
