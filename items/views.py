from unicodedata import category
from django.shortcuts import render

from items.models import Item, ItemCategory, ItemImages
from items.serializers import ItemCategorySerializer, ItemImageSerializer, ItemSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
  page_size = 8
  page_size_query_param = 'page_size'
  max_page_size = 16

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['title', 'sku', 'code', 'stock', 'category']
  pagination_class = CustomPagination
  
class ItemCategoryViewSet(viewsets.ModelViewSet):
  queryset = ItemCategory.objects.all()
  serializer_class = ItemCategorySerializer
  
class ItemImageViewSet(viewsets.ModelViewSet):
  queryset = ItemImages.objects.all()
  serializer_class = ItemImageSerializer
