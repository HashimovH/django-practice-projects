from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('estates/', views.estates, name="estates"),
    path('estate/<str:pk>', views.detail, name="detail"),
    path('review/submit/', views.submitReview, name="submitReview"),
    path('inquiry/submit/<int:estate>', views.submitRequest, name="submitRequest"),
    # path('search/', views.search, name="search"),
]