"""review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import testapp.views
import portfolio.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testapp.views.home, name="home"),
    path('blog/<int:blog_id>', testapp.views.detail, name="detail"),
    path('new/',testapp.views.new,name="new"),
    path('create/',testapp.views.create,name="create"),

    path('portfolio/', portfolio.views.portfolio, name="portfolio")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <type:name> 여러객체를 다루는 계층적 url 필요시 사용
# path-converter

# path의 create.html 로드하는 것이 아니라 
# views.py의 create 함수를 호출하라는 의미 !
# path 와 html 갯구가 비례하지 않는다 !