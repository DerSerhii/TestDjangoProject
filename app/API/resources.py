from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.API.serializers import BookSerializer, AuthorWriteSerializer, AuthorReadSerializer, \
    AuthorBookIdSerializer
from app.models import Book, Author


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(title=f"{serializer.validated_data.get('title')}!")

    def get_queryset(self):
        queryset = Book.objects.all()
        author_age = self.request.query_params.get('author_age')

        if author_age and author_age.isdigit():
            queryset = queryset.filter(author__age__gte=int(author_age))
        return queryset


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AuthorReadSerializer
        return AuthorWriteSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        book_name = self.request.query_params.get('book_name')

        if book_name:
            queryset = queryset.filter(book__title__icontains=book_name)
        return queryset

    @action(detail=True, methods=['get'])
    def author_with_books_id(self, request, pk=None):
        author = self.get_object()
        serializer = AuthorBookIdSerializer(author)
        return Response(serializer.data)
