
from django.urls import path
from app01 import views


# app_name = 'aaa'
urlpatterns = [
    # path('admin/', admin.site.urls),   django 2.0 不用url了
    # path('^$',views.index),
    path('2',views.index),  # 测试

]
