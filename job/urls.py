from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
    
)
from . import views

urlpatterns = [
	path('', views.index, name='job-index'),
    path('jobs/', PostListView.as_view(), name='job-jobs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='job-about'),
	path('apply/', views.apply, name='job-apply'),
	path('interview/', views.interview, name='job-interview'),
	path('announcement/', views.announcement, name='job-announcement'),
	path('motivate/', views.motivate, name='job-motivate'),
]