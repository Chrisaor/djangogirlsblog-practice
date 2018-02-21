from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('add/', views.post_add, name='post-add'),
]