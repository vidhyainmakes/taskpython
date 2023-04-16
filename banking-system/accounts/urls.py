from django.urls import path

from .views import UserRegistrationView, LogoutView, UserLoginView, UserBranchesView

app_name = 'accounts'

urlpatterns = [
    path("login/", UserLoginView.as_view(),name="user_login"),
    path("logout/", LogoutView.as_view(),name="user_logout"),
    path("register/", UserRegistrationView.as_view(),name="user_registration"),
    path("branches/", UserBranchesView.as_view(),name="user_branches"),
]
