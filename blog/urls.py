from django.conf.urls import url
from . import views


'''
Assign a view called 'post_list' to the url ^$
'''
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]