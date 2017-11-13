from django.conf.urls import url
from . import views


'''
Assign a view called 'post_list' to the url ^$
'''
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	# For http://127.0.0.1:8000/post/1/, we have -- 
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

''' 
(?P<pk>\d+) – this part is trickier. It means that Django will take
everything that you place here and transfer it to a view as a variable called
pk. (Note that this matches the name we gave the primary key variable back in
blog/templates/blog/post_list.html!) \d also tells us that it can only be a
digit, not a letter (so everything between 0 and 9). + means that there needs
to be one or more digits there. So something like http://127.0.0.1:8000/post//
is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK! 
'''
