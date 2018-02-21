from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('detail/', views.post_detail, name='post-detail'),
]