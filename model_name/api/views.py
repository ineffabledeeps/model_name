from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from model_name.models import classroom, timetable
from rest_framework.views import APIView



@permission_classes((permissions.AllowAny,))
# def add_product(request):
#     ip = get_client_ip(request)
#     serializer = MyProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(requester_ip=ip)
#     return Response(serializer.data)
class ClassroomList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")
          
@permission_classes((permissions.AllowAny,))
class FacultyList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class FacultyList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")

@permission_classes((permissions.AllowAny,))
class Timetable(APIView):

    now = datetime.now()
    day=calendar.day_name[now.weekday()].lower()

    def get(self,request,status):
        rows=classroom.objects.filter(status=status).values_list('room_no',flat=True)
        filter = day + '__' + 'in'
        data = timetable.objects.filter(**{ filter: rows })#(details="room",tuesday__in=rows)
        
        serializer=TimetableSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")
