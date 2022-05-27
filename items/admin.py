from django.contrib import admin

from items.models import Item, ItemCategory, ItemImages

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemImages)
