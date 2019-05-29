from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
    DeleteView
	)
from django.contrib.auth.decorators import login_required
from .models import Post


def jobs(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'job/jobs.html', context)
	
class PostListView(ListView):
    model = Post
    template_name = 'job/jobs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
   
class PostDetailView(DetailView):
    model = Post	

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'salary', 'location', 'contact', 'duration', 'description', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'salary', 'location', 'contact', 'duration', 'description', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def apply(request):
	return render(request, 'job/apply.html')

@login_required
def announcement(request):
	return render(request, 'job/announcement.html')

def about(request):
	return render(request, 'job/about.html')

def index(request):
	return render(request, 'job/index.html')

def interview(request):
	return render(request, 'job/interview.html')

def motivate(request):
	return render(request, 'job/motivate.html')