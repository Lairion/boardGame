from rest_framework.routers import SimpleRouter
from rooms.api import views
router = SimpleRouter()

router.register('room', views.RoomViewSet)
urlpatterns = router.urls
