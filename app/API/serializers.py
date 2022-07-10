from rest_framework import serializers
from app.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class AuthorReadSerializer(serializers.ModelSerializer):
    books = BookTitleSerializer(many=True, source='book_set', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'books']


class AuthorBookIdSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, source='book_set', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'books']


class AuthorWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']
