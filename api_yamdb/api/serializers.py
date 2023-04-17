from rest_framework import serializers

from reviews.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        model = Category
        exclude = ('id',)
