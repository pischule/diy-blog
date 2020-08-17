from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Blogger, Blog, Comment


# Create your views here.


def index(request):
    num_bloggers = Blogger.objects.all().count()
    num_blogs = Blog.objects.all().count()
    num_comments = Comment.objects.all().count()

    context = {
        'num_bloggers': num_bloggers,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
    }

    return render(request, 'index.html', context=context)


class BlogsListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = Blogger


class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogDetailView(generic.DetailView):
    model = Blog


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs.get('pk')})
