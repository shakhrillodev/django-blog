from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import all_news_view, Delete_News, Edit_News, detail_page_view, home_view, categories_view, per_category_view, regions_view, per_region_view, Create_News

urlpatterns = [
    path('', home_view, name='home'),
    path('all-news/', all_news_view, name='all_news'),
    path('categories/', categories_view, name='categories'),
    path('regions/', regions_view, name='regions'),
    path('detail/<int:pk>/', detail_page_view, name='detail'),
    path('category/<int:pk>/', per_category_view, name='category-news'),
    path('region/<int:pk>/', per_region_view, name='region-news'),
    path('create-news/', Create_News.as_view(), name='create_news'),
    path('edit/<int:pk>/', Edit_News.as_view(), name='edit_news'),
    path('delete/<int:pk>/', Delete_News.as_view(), name='delete_news')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
