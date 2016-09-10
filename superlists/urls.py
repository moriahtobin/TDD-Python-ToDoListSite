from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
]
