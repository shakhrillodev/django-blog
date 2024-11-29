from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, News, Region
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home_view(request):
    return render(request, "home.html", {
        "first_news": News.objects.first(),
        "three_news": News.objects.all().order_by('-date')[:3]
    })

def all_news_view(request): 
    all_news = News.objects.all()
    return render(request, "all-news.html", {
        "all_news": all_news
    })

def regions_view(request):
    regions = Region.objects.all()
    return render(request, 'regions-page.html', {
        'regions': regions
    })

def per_region_view(request,pk):
    region = Region.objects.get(id=pk)
    region_news = News.objects.filter(region=region)
    return render(request, 'region-news.html', {
        'region': region,
        'region_news': region_news
    })


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories-page.html', {
        'categories': categories
    })

def per_category_view(request, pk):
    category = Category.objects.get(id=pk)
    category_news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'category': category,
        'category_news': category_news
    })


def detail_page_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    category = Category.objects.get(id=news.category.id)
    region_news = News.objects.filter(category=category).exclude(id=pk)
    context = {
        'news': news,
        'category': category,
        'region_news': region_news 
    }

    return render(request, 'detail.html', context)

class Create_News(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = News
    template_name = 'create_news.html'
    fields = ['category', 'region', 'title', 'text', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser

class Edit_News(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = News
    template_name = 'edit-news.html'
    fields = ['category', 'region', 'title', 'text']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author== self.request.user

class Delete_News(LoginRequiredMixin, DeleteView): 
    model = News
    template_name = 'delete-news.html'
    success_url = reverse_lazy('home')