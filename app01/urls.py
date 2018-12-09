from django.conf.urls import url
from django.urls import path
from app01 import views


# app_name = 'aaa'
urlpatterns = [
    # path('^$',views.index),
    url('^$',views.index),
    url(r'2', views.hehe),
    # path('2',views.index),  # 测试
    # url('qrcode1/',views.showImg)

]
