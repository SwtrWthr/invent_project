from rest_framework import serializers
from stocks.models import Stock, StockType
from users.serializers import ProfileSerializer, UserSerializer

class StockTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = StockType
    fields = '__all__'
    
    
class StockSerializer(serializers.ModelSerializer):
  # managers = serializers.StringRelatedField(many=True)
  managers = UserSerializer(many=True, read_only=True).data
  type = StockTypeSerializer(many=False, read_only=True)
  class Meta:
    model = Stock
    fields = '__all__'
    
class UserStocksSerializer(serializers.ModelSerializer):
  type = StockTypeSerializer(many=False, read_only=True)
  
  class Meta:
    model = Stock
    fields = ('id', 'title', 'description', 'capacity', 'type', 'is_active',)