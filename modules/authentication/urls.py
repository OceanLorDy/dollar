from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.signup, name="login"),
    path("index/", views.index, name="index"),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
