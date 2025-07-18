from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

@login_required
def home(request):
    context= {'posts': Post.objects.all()
            }   # This will fetch all posts from the database
    return render(request, 'blog/home.html',context)
@login_required
def about(request):
    return render(request, 'blog/about.html')

class PostListView(LoginRequiredMixin,ListView):
    model= Post
    template_name='blog/home.html'
    context_object_name= 'post'

class PostDetailView(LoginRequiredMixin,DetailView):
    model= Post
    template_name='blog/post_detail.html'
    context_object_name= 'post'

    def get_queryset(self):
        qs = super().get_queryset()
        #print(qs.query)  # View SQL in console
        return qs

class PostCreateView(LoginRequiredMixin,CreateView):
    pass
    model=Post
    fields=['title','content']
    #success_url = reverse_lazy('post-detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
      model=Post
      fields= ['title','content']
      
      def form_valid(self, form):
          #form.instance.author=self.request.user
          return super().form_valid(form)
      
      def test_func(self):
          post = self.get_object()
          return self.request.user == post.author
      

class PostDeleteView(LoginRequiredMixin,DeleteView ):
    pass