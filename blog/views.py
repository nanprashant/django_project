from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,DetailView
# Create your views here.
posts=[
        {            'author': 'John Doe',
            'title': 'Blog Post 1',   
            'content': 'This is the content of blog post 1.',   
            'date_posted': 'January 1, 2023'
        },
        {  'author': 'Jane Smith',
            'title': 'Blog Post 2',   
            'content': 'This is the content of blog post 2.',   
            'date_posted': 'February 1, 2023' 

        }
]
@login_required
def home(request):
    context= {'posts': Post.objects.all()
            }   # This will fetch all posts from the database
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model= Post
    template_name='blog/home.html'
    context_object_name= 'post'

class PostDetailView(DetailView):
    model= Post
    template_name='blog/post_detail.html'
    context_object_name= 'post'

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs.query)  # View SQL in console
        return qs


    