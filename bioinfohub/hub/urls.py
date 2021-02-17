from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about-us"),
    path('authors/', views.authors, name="authors"),
    path('authors/<str:pk>', views.authorDetail, name="author-detail"),
]