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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

import testapp.views
import portfolio.views
import accounts.views
import employee.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testapp.views.home, name='home'),

    path('testapp/', include('testapp.urls')),

    path('accounts/', include('accounts.urls')),

    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    
    path('employee/', include('employee.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# <type:name> 여러객체를 다루는 계층적 url 필요시 사용
# path-converter

# path의 create.html 로드하는 것이 아니라 
# views.py의 create 함수를 호출하라는 의미 !
# path 와 html 갯구가 비례하지 않는다 !