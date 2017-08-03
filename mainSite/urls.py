from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # offer id
    url(r'^(?P<shoe_id>[0-9]+)/$', views.detail, name='detail')
]
