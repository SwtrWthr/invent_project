from email.policy import default
import uuid
from django.db import models
from stocks.models import Stock
from cloudinary.models import CloudinaryField


class ItemCategory(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=512)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = "item_categories"

  def __str__(self):
    return self.title


class Item(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=1024, null=True, blank=True)
  availability = models.IntegerField(default=0)
  sku = models.CharField(max_length=100, null=True)
  code = models.CharField(max_length=256, null=True)
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
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  # item = models.ImageField(default=0)
  image = CloudinaryField("image")
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = "item_images"

  @property
  def image_url(self):
    return (
      f"https://res.cloudinary.com/djdo3ud0z/{self.image}"
    )

  def __str__(self):
    return self.title
