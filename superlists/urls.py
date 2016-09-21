from django.conf.urls import url

#url syntax (regex, view, kwargs (default None), name (default None))
#r signals string as regex to python r'' is Any, r'^$' is Empty
urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list',
        name='view_list'),
    #url(r'^lists/new/$', 'lists.views.new_list', name='new_list'),
]
