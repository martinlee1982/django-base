"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#这是整个工程的路由urls，它可以通过include来指向子应用的路由urls,当工程里面创建多个子应用时，工程路由url可以指向指定的字应用路由url
from django.contrib import admin
from django.urls import path,include
from book import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('book.urls')), #此时通过http://127.0.0.1:8000/index/将访问不到子应用中views中的页面，只能通过http://127.0.0.1:8000/blog/index/访问到，即通过工程路由+子应用路由的方式访问
    #在这里path('blog/',include('book.urls'))改为path('',include('book.urls'))，就可以通过http://127.0.0.1:8000/index/访问到子应用的页面

]
