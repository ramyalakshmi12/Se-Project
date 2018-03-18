from django.conf.urls import url
from . import views
from logins import views as v

urlpatterns = [
	url(r'^$', views.book, name='book'),
	url(r'^signin/$', v.signin, name='signin'),
	url(r'^signup/$', v.signup, name='signup'),
	url(r'postsignin/$', v.postsignin, name='postsignin'),
	url(r'postsignup/$', v.postsignup, name='postsignup'),
	url(r'postbooking/$', views.postbooking, name='postbooking'),
	url(r'logout/$', v.logout, name='logout'),
	url(r'^profile/$', v.profile, name='profile')
    ]
