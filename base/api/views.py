from rest_framework.decorators import api_view
from rest_framework.response import Response
from base import models
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes =[
        "GET/api",
        "GET/api/rooms",
        "GET/api/rooms/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = models.Room.objects.all()
    seralizer = RoomSerializer(rooms,many=True)
    return Response(seralizer.data)

@api_view(['GET'])
def getRoom(request,id):
    room = models.Room.objects.get(id=id)
    seralizer = RoomSerializer(room,many=False)
    return Response(seralizer.data)