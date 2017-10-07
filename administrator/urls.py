from django.conf.urls import url
from administrator import views
from django.contrib.auth import views as auth_views

app_name = 'administrator'


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^add-news/$', views.add_news, name='add-news'),
    url(r'^view-news/$', views.view_news, name='view-news'),
    url(r'^edit-news/(?P<pk>[0-9]+)/', views.UpdateNews.as_view(), name='update-news'),
    url(r'^delete-news/(?P<pk>[0-9]+)/', views.delete_news, name='delete-news'),
    url(r'^add-event/$', views.add_event, name='add-event'),
    url(r'^view-events/$', views.view_events, name='view-events'),
    url(r'^edit-event/(?P<pk>[0-9]+)/', views.EventUpdate.as_view(), name='update-event'),
    url(r'^delete-event/(?P<pk>[0-9]+)/', views.delete_event, name='delete-event'),
    url(r'^add-teacher/$', views.add_teacher, name='add-teacher'),
    url(r'^view-teachers/$', views.view_teachers, name='view-teachers'),
    url(r'^edit-teacher/(?P<pk>[0-9]+)/', views.TeacherUpdate.as_view(), name='update-teacher'),
    url(r'^delete-teacher/(?P<pk>[0-9]+)/', views.delete_teacher, name='delete-teacher'),
    url(r'^add-executive/$', views.add_executive, name='add-executive'),
    url(r'^view-executives/$', views.view_executives, name='view-executives'),
    url(r'^edit-executive/(?P<pk>[0-9]+)/', views.ExecutiveUpdate.as_view(), name='update-executive'),
    url(r'^delete-executive/(?P<pk>[0-9]+)/', views.delete_executive, name='delete-executive'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile-update/$', views.update_profile, name='update-profile'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, 
    {'next_page': '/administrator/login/'}, name='logout'),
    
]
