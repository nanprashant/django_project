from django.urls import path
from .views import home
from .views import about
from .views import PostListView,PostDetailView

urlpatterns = [
    
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about', about, name='blog-about'),
    
]
