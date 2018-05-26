from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new_form/$', views.new_form, name='new_form'),
]
