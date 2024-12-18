from django.urls import include, path
from .views import NewsListView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', NewsListView.as_view(), name="newslist"),
]