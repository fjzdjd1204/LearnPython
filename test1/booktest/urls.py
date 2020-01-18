from django.conf.urls import url
from booktest import views

urlpatterns = [
    # url 路由配置
    url(r'^index$', views.index),

    url(r'^subpage$', views.subpage),

    url(r'^books$', views.show_books),

    url(r'^books/(\d+)$', views.detail),
]
