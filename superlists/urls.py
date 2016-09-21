from django.conf.urls import include, url

#url syntax (regex, view, kwargs (default None), name (default None))
#r signals string as regex to python r'' is Any, r'^$' is Empty
urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
]
