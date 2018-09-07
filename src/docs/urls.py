from django.conf.urls import url

from .views import schema_view

urlpatterns = [
    url(r'^', schema_view, name='index')
]
