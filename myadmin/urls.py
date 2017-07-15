from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'myadmin'

urlpatterns = [
    #url(r'^activity/$', views.activity, name='activity'),
#    url(r'^/change_aboutus/', views.change_team, name='change_team')

    url(r'^/check_user_pass/$', views.check_user_pass, name='check_user_pass'),
    url(r'^/login/$', views.login_user, name='login_user'),
    url(r'^/upload/$', views.upload, name='upload'),
    url(r'^/logout/$', views.logout_user, name='logout_user'),
    url(r'^/$', views.adminindex, name='adminindex'),
    url(r'^/filters/activ$', views.activ, name='activ'),
    url(r'^/filters/monitor$', views.monitor, name='monitor'),
    url(r'^/filters/slider$', views.slider, name='slider'),
    url(r'^/partners/$', views.partners, name='partners'),
    url(r'^/news/$', views.news, name='news'),
    url(r'^/partners_add/$', views.partners_add, name='partners_add'),
    url(r'^/partners_add_save/$', views.partners_add_save, name='partners_add_save'),
    url(r'^/partners_update/(?P<id>[0-9]+)$', views.partners_update, name='partners_update'),
    url(r'^/partners_update_save/(?P<id>[0-9]+)$', views.partners_update_save, name='partners_update_save'),
    url(r'^/partners_delete/(?P<id>[0-9]+)$', views.partners_delete, name='partners_delete'),
    url(r'^/news_add/$', views.news_add, name='news_add'),
    url(r'^/news_update/(?P<id>[0-9]+)$', views.news_update, name='news_update'),
    url(r'^/news_delete/(?P<id>[0-9]+)$', views.news_delete, name='news_delete'),
    url(r'^/news_update_save/(?P<id>[0-9]+)$', views.news_update_save, name='news_update_save'),
    url(r'^/reference/$', views.reference, name='reference'),
    url(r'^/reference_add/$', views.reference_add, name='reference_add'),
    url(r'^/reference_add_save/$', views.reference_add_save, name='reference_add_save'),
    url(r'^/reference_update/(?P<id>[0-9]+)$', views.reference_update, name='reference_update'),
    url(r'^/reference_update_save/(?P<id>[0-9]+)$', views.reference_update_save, name='reference_update_save'),
    url(r'^/reference_delete/(?P<id>[0-9]+)$', views.reference_delete, name='reference_delete'),
    url(r'^/team/$', views.team, name='team'),
    url(r'^/team/add/$', views.team_add, name='team_add'),
    url(r'^/team/team_change/(?P<id>[0-9]+)$', views.team_change, name='team_change'),
    url(r'^/team/team_delete/(?P<id>[0-9]+)$', views.team_delete, name='team_delete'),
    url(r'^/change_aboutus/', views.change_aboutus, name='change_aboutus'),
    url(r'^/about/$', views.about, name='about'),
    url(r'^/contacts/$', views.contacts, name='contacts'),
    url(r'^/change_contacts/', views.change_contacts, name='change_contacts'),
    url(r'^/users/$', views.users, name='users'),
    url(r'^/user_add/$', views.user_add, name='user_add'),
    url(r'^/user_add_save/$', views.user_add_save, name='user_add_save'),
    url(r'^/user_update_save/(?P<id>[0-9]+)$$', views.user_update_save, name='user_update_save'),
    url(r'^/user_update/(?P<id>[0-9]+)$$', views.user_update, name='user_update'),
    url(r'^/user_delete/(?P<id>[0-9]+)$$', views.user_delete, name='user_delete'),
    url(r'^/image/$', views.image, name='image'),
    url(r'^/image/add/$', views.image_add, name='image_add'),
    url(r'^/image/image_change/(?P<id>[0-9]+)$', views.image_change, name='image_change'),
    url(r'^/image/image_delete/(?P<id>[0-9]+)$', views.image_delete, name='image_delete'),
]
