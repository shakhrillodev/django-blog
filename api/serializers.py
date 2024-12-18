from rest_framework.serializers import ModelSerializer
from app.models import  News

class NewsSerializer(ModelSerializer):
    class Meta: 
        model = News
        fields = [
            "category",
            "region",
            "title",
            "text",
            "image",
            "date",
            "author",
        ]
        depth = 1
