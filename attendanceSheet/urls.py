from django.conf.urls import url
from . import views

app_name = 'collaAdmin'
#name the app

urlpatterns=[
    url(r'^userProfile/$',views.userProfiles_views,name='uerProfile'),
    url(r'^userAttendance/$',views.userAttendance_views,name='userAtd'),

]