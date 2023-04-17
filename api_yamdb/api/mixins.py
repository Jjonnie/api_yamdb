from rest_framework import filters, mixins, viewsets

from .permissions import AnonimCanReadOnly, IsSuperUserOrIsAdminOnly

class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    """Вьюсет, позволяющий осуществлять GET, POST, DELETE запросы."""
    
    permission_classes = [AnonimCanReadOnly, IsSuperUserOrIsAdminOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'