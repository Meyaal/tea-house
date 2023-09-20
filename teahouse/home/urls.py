from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feature/', views.feature, name='feature'),
    # path('products/', views.products, name='products'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.notFound, name='404'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy, name='privacy')
]
