from django.urls import path
from .views import home
from .views import about
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about', about, name='blog-about'),
    path('create', PostCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/',PostUpdateView.as_view(), name='blog-update')
    
]
