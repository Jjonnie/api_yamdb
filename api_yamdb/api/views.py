from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from reviews.models import Comment, Review, Title
from reviews.pagination import CommentsPagination, ReviewsPagination
from reviews.permissions import IsSuperUserIsAdminIsModeratorIsAuthor

from .serializers import CommentSerializer, ReviewSerializer, TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class AllReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = ReviewsPagination
    permission_classes = [IsSuperUserIsAdminIsModeratorIsAuthor]

    def get_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def get_queryset(self):
        title = self.get_title()
        reviews = title.reviews.all()
        return reviews

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(author=self.request.user, title=title)


class AllCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CommentsPagination
    permission_classes = [IsSuperUserIsAdminIsModeratorIsAuthor]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review_obj = get_object_or_404(Review, id=review_id, title=title_id)
        return Comment.objects.filter(review=review_obj)

    def get_review(self):
        review_id = self.kwargs.get('review_id')
        return get_object_or_404(Review, id=review_id)

    def get_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def perform_create(self, serializer):
        review = self.get_review()
        title = self.get_title()
        if title != review.title:
            raise NotFound()
        serializer.save(author=self.request.user, review=review)
