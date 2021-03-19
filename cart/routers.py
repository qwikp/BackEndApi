from rest_framework import routers
from .views import CartViewset,CartItemViewset

router = routers.DefaultRouter()
router.register(r'/carts',CartViewset )
router.register(r'/cart_items',CartItemViewset )