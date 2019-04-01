from rest_framework.routers import SimpleRouter
from turns.api import views
router = SimpleRouter()

router.register('turn', views.TurnViewSet)
urlpatterns = router.urls
