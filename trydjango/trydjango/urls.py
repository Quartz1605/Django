"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import home
from articles import views
from accounts.views import login_view,logout_view,register_view


#Uske pehle slash daalne ki jarurat nahi hai wo apne aap provide hota hai.
# Basically usse import kiya and then created a url for it.

urlpatterns = [
    
    path('',home),
    
    path('admin/', admin.site.urls),
    path('articles/',views.article_search_view),
    path('articles/create/',views.article_create_view),
    path('articles/<int:id>/',views.article_detail_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view)
    
]

## <int:id> isme id just name hai.
