__all__ = ['GENERIC_MODEL_URL', 'GENERIC_MODEL_VIEW']


GENERIC_MODEL_URL = """from rest_framework.routers import SimpleRouter
from {{ app }}.api import views
router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}
urlpatterns = router.urls
"""
GENERIC_MODEL_URL_V2 = """from rest_framework.routers import SimpleRouter
from {{ app }}.api import views
router = SimpleRouter()
{% for model in models %}
router.register('{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}
urlpatterns = router.urls
"""

GENERIC_MODEL_VIEW = """from rest_framework import viewsets,mixins
from {{ app }}.api.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}
class {{ model }}ViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
{% endfor %}"""