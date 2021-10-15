from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.models import Book
from api.serializers import BookSerializer


class BookFilter(filters.FilterSet):
    age_group = filters.CharFilter()
    author_id = filters.NumberFilter(method='filter_author_id')
    genre = filters.CharFilter()
    read = filters.BooleanFilter()
    series_id = filters.NumberFilter()

    def filter_author_id(self, queryset, name, value):
        return queryset.filter(authors__id=value)


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter