from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from items.views import ItemCategoryViewSet, ItemImageViewSet, ItemViewSet

from stocks.views import StockTypeViewSet, StockViewSet, UserStocksViewSet
from users.views import LogoutView, ProfileViewSet, RoleViewSet, UserViewSet

router = routers.SimpleRouter()
router.register('stock_types', StockTypeViewSet)
router.register('my_stocks', UserStocksViewSet)
router.register('stocks', StockViewSet)
router.register('users', UserViewSet)
router.register('roles', RoleViewSet)
router.register('items', ItemViewSet)
router.register('item_categories', ItemCategoryViewSet)
router.register('item_images', ItemImageViewSet)
# router.register('profile', ProfileViewSet, basename="profile-detail")

schema_view = get_swagger_view(title='Invent API')

urlpatterns = [
  path('api/docs', schema_view),
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('api/me/', ProfileViewSet.as_view(), name='current_user'),
  path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/logout/', LogoutView.as_view(), name='user_logout'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
