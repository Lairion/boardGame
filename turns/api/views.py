from rest_framework import viewsets,mixins
from turns.api.serializers import TurnSerializer
from turns.models import Turn

class TurnViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
