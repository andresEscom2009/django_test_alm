from rest_framework.routers import DefaultRouter
from posts.api.views import PostModelViewSet
from posts.api.views import ArticleModelViewSet

router_post = DefaultRouter()
router_post.register(prefix=r'posts', basename='posts', viewset=PostModelViewSet)

router_article = DefaultRouter()
router_article.register(prefix=r'article', basename='article', viewset=ArticleModelViewSet)
