from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class ArticleCreateView(CreateView, LoginRequiredMixin):
    model=models.Article
    template_name='article_new.html'
    fields =['title','body']
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class ArticleListView(ListView, LoginRequiredMixin):
    model = models.Article
    template_name = "article_list.html"
    login_url = 'login'

class ArticleUpdateView(UpdateView, LoginRequiredMixin):
    model = models.Article

    fields =['title','body']

    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDetailView(DetailView, LoginRequiredMixin):
    model = models.Article

    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    model = models.Article


    template_name = 'article_delete.html'

    success_url = reverse_lazy('article_list')

    login_url = 'login'
