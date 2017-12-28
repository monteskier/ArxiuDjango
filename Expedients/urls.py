from django.conf.urls import include, url


urlpatterns = [
      url(r'^$', 'Expedients.views.home', name='home'),
]
