"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from main import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken import views as authviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'mains', views.MainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name="signup"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('home',views.home,name="home"),
     path('', include(router.urls)),
     path('api-token-auth/', authviews.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
