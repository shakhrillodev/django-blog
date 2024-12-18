from django.urls import include, path
from .views import NewsListView, DetailView, UpdateView, DeleteView, ActionView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<int:pk>/', DetailView.as_view(), name="news-detail"),
    path('<int:pk>/update/', UpdateView.as_view(), name="news-update"),
    path('<int:pk>/delete/', DeleteView.as_view(), name="news-delete"),
    path('<int:pk>/action/', ActionView.as_view(), name="news-action"),
    path('', NewsListView.as_view(), name="newslist"),
]