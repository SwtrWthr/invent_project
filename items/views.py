from django.http import Http404
from items.models import Item, ItemCategory, ItemImages
from items.serializers import CreateItemSerializer, ItemCategorySerializer, ItemDetailSerializer, ItemImageSerializer, ItemSerializer
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django_filters import CharFilter
from django_filters import rest_framework as filters

import cloudinary
from items.utils import generate_qr_code


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
  
  def get_serializer_class(self):
    if self.action == 'create':
      return CreateItemSerializer
    if self.action == 'update':
      return CreateItemSerializer
    return ItemSerializer
  
  def perform_create(self, serializer):
    item = serializer.save()
    
    try:
      qr_code = generate_qr_code(item.id)
      uploaded_image = cloudinary.uploader.upload_resource(qr_code, folder='qr/')
      created_item = Item.objects.get(pk=item.id)
      created_item.qr_code = uploaded_image.url
      created_item.save()
    except Exception:
      raise APIException('Товар создан. Но не удалось создать QR code')
    
  def perform_update(self, serializer):
    instance = serializer.save()
    
    if not instance.qr_code:
      try:
        qr_code = generate_qr_code(instance.id)
        uploaded_image = cloudinary.uploader.upload_resource(qr_code, folder='qr/')
        created_item = Item.objects.get(pk=instance.id)
        created_item.qr_code = uploaded_image.url
        created_item.save()
        
        return Response(created_item, status=status.HTTP_200_OK)
      except Exception:
        raise APIException('Не удалось создать QR code')
  
  @action(detail=True, methods=['GET'], name='Item Detail')
  def detailed(self, request, pk=None):
    try:
      item = Item.objects.get(pk=pk)
    except Exception:
      raise Http404
    # queryset = get_object_or_404(Item, pk=pk)
    serializer = ItemDetailSerializer(item)
    
    # if serializer.is_valid():
    return Response(serializer.data)
    # else:
      # return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
  
class ItemCategoryViewSet(viewsets.ModelViewSet):
  queryset = ItemCategory.objects.all()
  serializer_class = ItemCategorySerializer
  
class ItemImageViewSet(viewsets.ModelViewSet):
  queryset = ItemImages.objects.all()
  parser_classes = (MultiPartParser,)
  serializer_class = ItemImageSerializer
