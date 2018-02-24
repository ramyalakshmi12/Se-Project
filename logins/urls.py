from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.base),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'postsignin/$', views.postsignin, name='postsignin'),
	url(r'postsignup/$', views.postsignup, name='postsignup'),
	url(r'logout/$', views.logout, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
]