from django.conf.urls import include,url
from . import views
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^hoods', views.neibahoods, name='hoods'),  
    url(r'^new/post$', views.new_post, name='newpost'),  
    url(r'^join/(\d+)',views.join,name='join'),
    url(r'^business/view',views.display_business,name = 'viewbiz'),
    url(r'^business/',views.create_business,name = 'business'),
]