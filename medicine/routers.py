from rest_framework import routers
from .views import MedicineViewset

router = routers.DefaultRouter()
router.register(r'medicines', MedicineViewset)