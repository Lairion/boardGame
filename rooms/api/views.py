from rest_framework import viewsets,mixins
from rooms.api.serializers import RoomSerializer
from rooms.models import Room
from rest_framework.response import Response
from rest_framework.decorators import action
from turns.models import Turn

def find_empty_position(string,value,last_pos,room):
    if last_pos>=len(string):
        return -1
    position = string.find(value,last_pos)
    if position>=0:
        if Turn.objects.filter(room=room,card_position=position).exists():
            return find_empty_position(string,value,position+1,room)
    return position

def get_last_position(string,card,last_pos,room):
    count_color = 0
    position = last_pos
    for i in list(card):
        position = find_empty_position(string,i,position+count_color,room)
        count_color = 1
        if position<0:
            break

    return position

class RoomViewSet(mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(methods=['POST'], detail=False,url_path='create-room', url_name='create-room')
    def create_room(self,request):
        data = request.data
        players = [["player "+str(i+1),0] for i in range(int(data["number_of_players"]))]
        current_player = 0
        deck = data.pop("deck").split(', ')
        combo = data.pop("combo")
        room = Room.objects.create(**data)
        turn = 0
        winner = "No winner"
        for card in deck:
            players[current_player][1] = get_last_position(combo,card,players[current_player][1],room)
            Turn.objects.create(
                    room=room,
                    player_name=players[current_player][0],
                    card_value=card,
                    card_position=players[current_player][1] )
            if players[current_player][1]>=0 and (not players[current_player][1] == len(combo)-1):
                current_player += 1
                if current_player>=len(players):
                   current_player = 0 
                turn += 1
                continue
            else:
                winner = "%s" % (players[current_player][0])
                break
        room.result = winner + " after %s turn" % (turn)
        room.save()
        room_serial = self.get_serializer(data=room)
        room_serial.is_valid()
        return Response(data = room_serial.data )