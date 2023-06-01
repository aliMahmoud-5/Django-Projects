from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    context = {
        'posts': posts.objects.all()
    }
    return render(request,'Blog/home.html', context)


class postlist(ListView):
    model = posts
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2

class postdetail(DetailView):
    model = posts

class createpost(LoginRequiredMixin,CreateView):
    model = posts
    fields = ['title','content']
    

    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)



class updatepost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = posts
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.auth:
            return True

        return False

class deletepost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = posts
    success_url = 'blog-home'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.auth:
            return True

        return False