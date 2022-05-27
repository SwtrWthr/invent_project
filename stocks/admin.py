from django.contrib import admin

from stocks.models import Stock, StockType

admin.site.register(Stock);
admin.site.register(StockType);
