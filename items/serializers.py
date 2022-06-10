from rest_framework import serializers
from items.models import ItemImage, ItemCategory, Item


class ItemImageSerializer(serializers.ModelSerializer):
  image_url = serializers.ReadOnlyField()
  class Meta:
    model = ItemImage
    fields = ["image_url", "image", "created_at", "item"]

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation.pop("image")

    return representation


class ItemCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ItemCategory
    fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
  images = ItemImageSerializer(
    source='itemimages_set', many=True, read_only=True)
  category = ItemCategorySerializer(many=True, read_only=True)

  class Meta:
    model = Item
    fields = '__all__'
