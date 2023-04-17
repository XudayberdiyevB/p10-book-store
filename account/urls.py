from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import custom_login, profile, profile_edit, profile_delete, RegisterView

app_name = "account"

urlpatterns = [
    path("login/", custom_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    # path("<int:pk>/edit/", UserProfileUpdate.as_view(), name="profile_edit"),
    path("edit/", profile_edit, name="profile_edit"),
    path("delete/", profile_delete, name="profile_delete"),
    path("register/", RegisterView.as_view(), name="register")
]
