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
  images = ItemImageSerializer(source='itemimages_set', many=True, read_only=True)
  category = ItemCategorySerializer(many=True, read_only=True)
  class Meta:
    model = Item
    fields = '__all__'
