from django.urls import path, include
from . import views

urlpatterns = [
    path('compose/', views.createPost, name="create-post"),
    path('<str:pk>', views.postDetail, name="post-detail"),
    path('<str:pk>/edit', views.postEdit, name="post-edit"),
    path('<str:pk>/delete', views.postDelete, name="post-delete"),
    path('<str:pk>/save', views.postSave, name="post-save"),
    path('<str:pk>/save/delete', views.postSaveDelete, name="post-save-delete"),
]
