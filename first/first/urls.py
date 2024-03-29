"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webapp import views

urlpatterns = [
    path('todoEdit/<int:id>', views.todoEdit, name="todoEdit"),
    path('toEdit/<int:id>', views.toEdit, name='toEdit'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('authorization', views.authorization, name='authorization'),
	path('category', views.category, name="Category"),
    path('registration', views.registration, name='registration'),
    path('toAuthorization', views.getDataAuthorization),
    path('todo', views.todo),
    path('todoAdd', views.todoAdd, name='todoAdd'),
    path('todoDelete', views.todoDelete, name='todoDelete'),
    path('todoDone', views.todoDone, name='todoDone'),
    path('toRegistration', views.sendDataRegistration),

]
