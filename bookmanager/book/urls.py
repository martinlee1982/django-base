
#在每个字应用里面创建urls路由，在工程urls路由里面通过include方式与工程路由产生关系
from django.urls import path
from book.views import index
urlpatterns = [
    path('index/',index),

]