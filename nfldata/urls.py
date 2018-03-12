from django.conf.urls import url
from . import views


app_name = 'nfldata'
urlpatterns = [
    url(r'^add-nfldata/$', views.add_nfldata),
    url(r'^view-nfldata/$', views.view_nfldata),
    url(r'^view-teamdata/$', views.view_teamdata),
    url(r'^view-myteam/$', views.view_myteam),
    url(r'^view-draftresults/$', views.view_draftresults),
    url(r'^begin-draft/$', views.begin_draft),
    url(r'^$', views.index, name='index')
]
