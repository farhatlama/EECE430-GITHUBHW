from django.urls import path
from . import views

app_name = "myapp1"
urlpatterns = [
    path('', views.menu, name='menu'),
    path('videos/', views.video_list, name='list'),
    path('videos/create/', views.video_create, name='create'),
    path('videos/<int:pk>/', views.video_detail, name='detail'),
    path('videos/<int:pk>/edit/', views.video_update, name='update'),
    path('videos/<int:pk>/delete/', views.video_delete, name='delete'),
]
