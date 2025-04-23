from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView

urlpatterns = [
    #path("fbv-index", views.indexView , name= 'fbv-test'),
    #path('cbv-index', TemplateView.as_view(template_name = 'index.html' , extra_context = {'name' :'ali'}))
    path('cbv-index' ,views.IndexView.as_view() , name='cbv-index' ),
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com/"),name="go-to-django",),
    path("go-to-index/", RedirectView.as_view(pattern_name ="cbv-index"),name="go-to-index",),
    path('posts/' , views.PostListView.as_view() , name = 'posts-list'),
    path('posts/<int:pk>/' , views.PostDetailView.as_view() , name = 'post-detail'),
    path('posts/create/' , views.PostCreateView.as_view() , name = 'post-create'),
    path('posts/<int:pk>/edit/' , views.PostEditView.as_view() , name = 'post-edit'),
    path('posts/<int:pk>/delete/' , views.PostDeleteView.as_view() , name = 'post-delete'),




]