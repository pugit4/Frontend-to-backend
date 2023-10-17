"""
URL configuration for Sports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Cricket import views

urlpatterns = [
    path('', views.players, name='home'),
    path('home_two', views.players_two, name="home_two"),
    path('add', views.add_players, name='add'),
    path('add2', views.add_players_two, name='add2'),
    path('update/<pk>', views.update_players, name='update'),
    path('update2/<pk>', views.update_players_two, name="update2"),
    path('delete/<pk>', views.delete_players, name="delete"),
    path('delete2/<pk>', views.delete_players_two, name="delete2"),
    path('admin/', admin.site.urls),
]
