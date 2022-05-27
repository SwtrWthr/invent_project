from rest_framework import viewsets
from items.views import CustomPagination

from stocks.models import Stock, StockType
from stocks.serializers import StockSerializer, StockTypeSerializer, UserStocksSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer
  pagination_class = CustomPagination
  # permission_classes = (IsAuthenticated, )
  
class UserStocksViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = UserStocksSerializer
  permission_classes = (IsAuthenticated, )
  authentication_classes = [JWTAuthentication]
  pagination_class = CustomPagination
  
  def get_queryset(self):
      return Stock.objects.filter(managers=self.request.user)
  
class StockTypeViewSet(viewsets.ModelViewSet):
  queryset = StockType.objects.all()
  serializer_class = StockTypeSerializer
  permission_classes = (IsAuthenticated, )
