from django.shortcuts import render
from.serializers import NewsSerializer
from app.models import News
from rest_framework.views import APIView, Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class NewsListView(APIView):
    def get(self, response):
        posts=News.objects.all()
        tests_serializer=NewsSerializer(posts, many=True)
        return Response(tests_serializer.data)
    
class DetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UpdateView (UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class DeleteView (DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ActionView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer