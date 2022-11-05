from django.urls import path
from . import views
from rest_framework.authtoken import views as view


urlpatterns = [
    path("accounts/", views.SellerView.as_view()),
    path("accounts/newest/<int:num>/", views.SellerDetailView.as_view()),
    path("login/", view.obtain_auth_token),
    path("accounts/<pk>/", views.SellerUpdateView.as_view()),
    path("accounts/<pk>/management/", views.AdminSellerUpdate.as_view()),
]
