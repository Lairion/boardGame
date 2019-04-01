from django.shortcuts import render

# Create your views here.
from rooms.models import Room
class RoomViews:
	
	@staticmethod
	def list_view(request):
		context = {
			"title":"Rooms"
		}
		return render(request,"rooms/rooms_page.html",context)

