from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("404/", views.notFound, name="404"),
    path("privacy", views.privacy, name="privacy"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
