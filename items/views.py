from items.models import Item, ItemCategory, ItemImages
from items.serializers import ItemCategorySerializer, ItemImageSerializer, ItemSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from django_filters import CharFilter
from django_filters import rest_framework as filters


class CustomPagination(PageNumberPagination):
  page_size = 8
  page_size_query_param = 'page_size'
  max_page_size = 16

class ItemFilter(filters.FilterSet):
  title = CharFilter(lookup_expr='icontains')
  code = CharFilter(lookup_expr='icontains')
  sku = CharFilter(lookup_expr='icontains')
  
  class Meta:
    model = Item
    fields = ['title', 'code', 'sku', 'stock', 'category']
class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = ItemFilter
  pagination_class = CustomPagination
  
class ItemCategoryViewSet(viewsets.ModelViewSet):
  queryset = ItemCategory.objects.all()
  serializer_class = ItemCategorySerializer
  
class ItemImageViewSet(viewsets.ModelViewSet):
  queryset = ItemImages.objects.all()
  parser_classes = (MultiPartParser,)
  serializer_class = ItemImageSerializer
