from rest_framework.serializers import ModelSerializer
from posts.models import Post
from posts.models import Article


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "order", "create_at"]
        # fields = __all__


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description", "type", "create_at"]
