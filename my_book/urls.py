
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show),
    url(r'^create$',views.create),
    url(r'^delete/(\d+)$',views.delete),
    url(r'^jc/$',views.jc_templates),
    url(r'^verify_code/$',views.verify_code),
]
