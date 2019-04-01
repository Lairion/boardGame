__all__ = ['MODEL_URL', 'MODEL_VIEW']


MODEL_URL = """from rest_framework.routers import SimpleRouter
from {{ app }}.api import views
router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}
urlpatterns = router.urls
"""
MODEL_URL_V2 = """from rest_framework.routers import SimpleRouter
from {{ app }}.api import views
router = SimpleRouter()
{% for model in models %}
router.register('{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}
urlpatterns = router.urls
"""


MODEL_VIEW = """from rest_framework.viewsets import ModelViewSet
from {{ app }}.api.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}
class {{ model }}ViewSet(ModelViewSet):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
{% endfor %}"""