from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("feature/", views.feature, name="feature"),
    path("store/", views.store, name="store"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("404/", views.notFound, name="404"),
    path("privacy", views.privacy, name="privacy"),
]
