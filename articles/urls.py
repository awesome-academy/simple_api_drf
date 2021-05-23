# Using with APIView and GenericView
#
#  from django.urls import path
# from .views import ArticleList, ArticleDetail

# urlpatterns = [
    # path("articles/", ArticleList.as_view(), name="articles_list"),
    # path("articles/<int:pk>/", ArticleDetail.as_view(), name="articles_detail"),
# ]

from articles.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
urlpatterns = router.urls
