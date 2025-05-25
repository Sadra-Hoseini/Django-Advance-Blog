from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic import ListView , DetailView , FormView , CreateView , UpdateView , DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def indexView(request):
    return render(request , 'index.html')




class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'sadra'
        context['posts'] = Post.objects.all()
        return context
    






class PostListView(LoginRequiredMixin,ListView):
    model = Post
    #queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    ordering = '-id'


""" def get_queryset(self):
        posts = Post.objects.filter()
        return posts"""






class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'







'''class PostCreateView(FormView):
    template_name = "post_form.html"
    form_class = PostForm
    success_url = "/blog/posts/"    


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)'''




class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #fields = ['author' , 'title' , 'content' , 'category' , 'published_date']
    form_class = PostForm
    success_url = "/blog/posts/" 

    #set author the curent user for form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/posts/"





class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = "/blog/posts/"    