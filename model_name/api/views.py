from asyncio.windows_events import NULL
from os import stat
from urllib import response
from .serializers import *
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.response import Response
from rest_framework import permissions
from model_name.models import classroom, timetable,dept
from rest_framework.views import APIView
from model_name.models import *
from model_name.models import faculties
from datetime import date
from rest_framework import status


@permission_classes((permissions.AllowAny,))
class ClassroomList(APIView):
    def get(self,request,status):
        data = classroom.objects.all().filter(status=status)
        serializer=ClassroomSerializer(data,context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self,request,status):
          return Response("in-progress")


          
# @permission_classes((permissions.AllowAny,))
# class FacultyList(APIView):
#     def get(self,request,status):
#         data = classroom.objects.all().filter(status=status)
#         serializer=ClassroomSerializer(data,context={'request': request}, many=True)
#         return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class FacultyList(APIView):
    def get(self,request):
        data = faculties.objects.all()
        serializer=FacultySerializer(data,context={'request': request}, many=True)
        
        return Response(serializer.data,)

    def post(self,request,status):
          return Response("in-progress")


@permission_classes((permissions.AllowAny,))
class Send_meeting_reqList(APIView):
    def post(self,request):   # kaam karna h 
        added=False
        prn = request.data["prn"]
        fac_id = request.data["fac_id"]
        time = meeting_req.objects.filter(prn=prn,fac_id=fac_id)
        if(len(time.values())>0):
            if (date.today() == time.values()[0]["updated_date"]):
                return Response("Can't Request Again!",status=status.HTTP_409_CONFLICT)
                # return Response("Cannot Request Again!")
            else:
                dept_id = students.objects.filter(prn=prn)
                req_store = meeting_req(prn = students.objects.get(prn=prn),
                                        fac_id=faculties.objects.get(fac_id=fac_id),
                                        dept_id=dept.objects.get(dept_id=dept_id.values()[0]["dept_id_id"]),
                                        status_req="requesting")
                req_store.save()
                added=True
        else:
            dept_id = students.objects.filter(prn=prn)
            req_store = meeting_req(prn = students.objects.get(prn=prn),
                                    fac_id=faculties.objects.get(fac_id=fac_id),
                                    dept_id=dept.objects.get(dept_id=dept_id.values()[0]["dept_id_id"]),
                                    status_req="requesting")
            req_store.save()
            added=True
        return Response({"added":added})
        #return Response(len(time.values())>0)


# Faculty Visibility

@permission_classes((permissions.AllowAny,))
class Set_meeting_reqList(APIView):
    def post(self,request,status):
        is_updated=False

        req_id = request.data["req_id"]
        if status=="accept":
            status="accepted"
        elif status=="decline":
            status="declined"
        else : status=False

        if(status):
            data = meeting_req.objects.filter(request_id=req_id).update(status_req=status) # setting on the basi of req_id
            is_updated=True
        return Response({"is_updated":is_updated})

@permission_classes((permissions.AllowAny,))
class Get_meeting_reqList(APIView):
    def post(self,request):
        fac_id = request.data["fac_id"]
        data = meeting_req.objects.all().filter(fac_id=fac_id) # fetching personalized req from table
        serializer=RequestListSerializer(data,context={'request': request}, many=True)

        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class Set_reqList(APIView):
    def post(self,request):
        fac_id = request.data["fac_id"]
        status = request.data["status"]
        prn = request.data["prn"]
        fetched_data = meeting_req.objects.all().filter(fac_id=fac_id,prn=prn,status=status) # fetching personalized req from table
        return Response(fetched_data.values())

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