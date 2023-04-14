from reviews.models import Genre
from .mixins import CreateListDestroyViewSet
from .serializers import GenreSerializer


class GenreViewSet(CreateListDestroyViewSet):
    """Вьюсет для создания обьектов класса Genre."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer