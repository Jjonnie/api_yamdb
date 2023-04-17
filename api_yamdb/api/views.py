from reviews.models import Category
from .mixins import CreateListDestroyViewSet
from .serializers import CategorySerializer


class CategoryViewSet(CreateListDestroyViewSet):
    """Вьюсет для создания обьектов класса Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer