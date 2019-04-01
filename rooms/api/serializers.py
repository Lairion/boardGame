from rest_framework import serializers 
from rooms.models import Room
from turns.api.serializers import TurnSerializer

class RoomSerializer(serializers.ModelSerializer):

    turns =TurnSerializer(many=True)
    def get_number_of_players(self, obj):
        return obj.players.all().count()
            
    class Meta:
        model = Room
        fields = '__all__'
