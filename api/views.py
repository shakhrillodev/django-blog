from django.shortcuts import render
from.serializers import NewsSerializer
from app.models import News
from rest_framework.views import APIView, Response
# Create your views here.

class NewsListView(APIView):
    def get(self, response):
        posts=News.objects.all()
        tests_serializer=NewsSerializer (posts, many=True)
        return Response(tests_serializer.data)