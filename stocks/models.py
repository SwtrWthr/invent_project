from django.db import models

from users.models import User

class StockType(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=512)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = "stock_types"
  
  def __str__(self):
      return self.title

class Stock(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=512)
  created_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  capacity = models.IntegerField(default=0)
  type = models.ForeignKey(StockType, on_delete=models.SET_NULL, null=True)
  managers = models.ManyToManyField(User, blank=True)
  
  class Meta:
    db_table = "stocks"
  
  def __str__(self):
      return self.title

