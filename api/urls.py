from django.conf.urls import url
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns=[
    url(r'^api/trabajos/$',views.TrabajosViewSet.as_view()),
    url(r'^api/trabajos_nombre/(?P<nombre>.+)/$',views.TrabajosFiltroViewSet.as_view()),
]