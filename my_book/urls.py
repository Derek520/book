
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show),
    url(r'^create$',views.create),
    url(r'^delete/(\d+)$',views.delete),
    url(r'^jc/$',views.jc_templates),
    url(r'^verify_code/$',views.verify_code),
    url(r'^verify_show/$',views.verify_show),
    url(r'^verify_yz/$',views.verify_yz),
    url(r'^fan1/$', views.fan1),
    url(r'^fan2/$', views.fan2),
    url(r'^fan_show/$', views.fan2, name='fan2'),
    url(r'^fan(\d+)_(\d+)/$', views.fan3,name='fan2'), # 带位置参数
    url(r'^fan(?P<id>\d+)_(?P<age>\d+)/$', views.fan4,name='fan2'), # 带关键字参数


]
