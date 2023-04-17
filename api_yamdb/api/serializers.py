from rest_framework import serializers
from reviews.models import Genre



class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор модели Genre."""

    class Meta:
        model = Genre
        exclude = ('id',)