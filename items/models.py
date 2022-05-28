from django.db import models
from stocks.models import Stock

class ItemCategory(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=512)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = "item_categories"
  
  def __str__(self):
      return self.title

class Item(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=512, null=True, blank=True)
  availability = models.IntegerField(default=0)
  sku = models.CharField(max_length=100, null=True)
  code = models.CharField(max_length=250, null=True, blank=True)
  stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
  rec_price = models.IntegerField(default=0, null=True)
  category = models.ManyToManyField(ItemCategory, blank=True)
  attrs = models.JSONField()
  received_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = "items"
  
  def __str__(self):
      return self.title

class ItemImages(models.Model):
  item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
  filename = models.CharField(max_length=150)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = "item_images"
  
  def __str__(self):
      return self.title

