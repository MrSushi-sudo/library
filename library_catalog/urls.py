from rest_framework.routers import DefaultRouter

from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls
