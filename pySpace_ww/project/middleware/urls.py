from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_update/$', views.register_update, name='register_update'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^index/$', views.index, name='index'),
    url(r'^message_update/$', views.message_update, name='message_update'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^history_data/$', views.history_data, name='^history_data'),
    url(r'^data_filter/$', views.data_filter, name='^data_filter'),
    url(r'^reg/$', views.reg, name = 'reg'),
    
    url(r'^logg/$', views.logg, name = 'logg'),
    url(r'^content/$', views.content, name='content'),
    url(r'^(?P<message_id>[0-9]+)/voteresults/$', views.voteresults, name='voteresults'),
    url(r'^(?P<message_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<message_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^regforapp/$', views.regforapp, name='regforapp'),
    url(r'^loginforapp/$', views.loginforapp, name='loginforapp'),
    url(r'^contentforapp/$', views.contentforapp, name='contentforapp'),
]