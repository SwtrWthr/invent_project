from rest_framework import serializers
from items.models import ItemImages, ItemCategory, Item

class ItemImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ItemImages
    fields = '__all__'
    
class ItemCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ItemCategory
    fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = '__all__'
