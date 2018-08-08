from django.conf.urls import url
from firstapp import views


app_name = 'first_app'

urlpatterns = [
	url(r'^$', views.hello, name='hello'),
	url(r'^django/$', views.django, name='django'),
	url(r'^bye/$', views.bye, name='bye'),
	url(r'^users/$', views.users, name='users'),
	url(r'^form/$', views.form_name_view, name='form'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^base/$', views.base, name='base'),
	url(r'^relative/$', views.relative, name='relative'),
	url(r'^other/$', views.other, name='other'),
	url(r'^registration/$', views.registration, name='registration'),
	url(r'^login/$', views.user_login, name='user_login')
] 

