"""
URL configuration for join_backend project.

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
from django.urls import path, include
from join.views import (
    TaskView,
    SingleTaskView,
    LoginView,
    LogoutView,
    CreateUserView,
    DeleteUserView,
    CategorysView,
    UserListView,
    ContactView,
    checkAuth,
)
from join.signals import receiver

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("check_auth/", checkAuth.as_view(), name="check_auth"),
    path("tasks/", TaskView.as_view(), name="tasks"),
    path("tasks/<int:task_id>/", SingleTaskView.as_view(), name="single_task"),
    path("categorys/", CategorysView.as_view(), name="categorys"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("create_user/", CreateUserView.as_view(), name="register"),
    path("delete_user/", DeleteUserView.as_view()),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("contacts/<int:contact_id>/", ContactView.as_view(), name="contacts_with_id"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path(
        "password_reset/confirm/",
        include("django_rest_passwordreset.urls", namespace="password_reset_confirm"),
    ),
]
