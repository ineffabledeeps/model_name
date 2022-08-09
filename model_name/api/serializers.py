from dataclasses import field
from datetime import date
from distutils.command.clean import clean
from xml.etree.ElementTree import tostring
from rest_framework import serializers
# from models import classroom, faculties, timetable
from datetime import datetime
import calendar
from model_name.models import meeting_req, students,faculties,classroom,timetable
import math


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = ('room_no', 'status', 'course_id', 'capacity', 'projector',
                  'ac', 'computer', 'desks', 'whiteboard', 'count', 'type')



class FacultySerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField('avail')

    def avail(self,obj):

        if(obj.availability==0):
            return True
        else:
            return False
    class Meta:
        model = faculties
        fields=('fac_id','fac_name','dept_id','fac_role','fac_cab_no','available')


class RequestListSerializer(serializers.ModelSerializer):

    details = serializers.SerializerMethodField('getStudentName')
   
    def getStudentName(self,obj):
        details = students.objects.filter(prn=obj.prn_id)
        semester = details.values()[0]['semester']
        year=math.ceil(int(semester)/2)
        return {"name":details.values()[0]['student_name'],"year":year}
    class Meta:
        model = meeting_req
        fields=('request_id', 'status_req', 'dept_id_id', 'fac_id_id', 'prn_id', 'updated_date','details')


class TimetableSerializer(serializers.ModelSerializer):
    more_details = serializers.SerializerMethodField('room_da')
    subject = serializers.SerializerMethodField('get_subject')


    global now 
    now= datetime.now()
    #current_time=now.strftime("%H:%M")
    global day
    day=calendar.day_name[now.weekday()].lower()


    class Meta:
        model = timetable
        fields = ('time','subject','dept_id_id','more_details')

    def get_subject(self,obj):
        subject = timetable.objects.all().filter(time=obj.time).filter(details="subject")
        return(subject.values(day)[0][day])

    def room_da(self, obj):
        room_query = timetable.objects.all().filter(time=obj.time).filter(details="room")
        room_no=room_query.values(day)[0][day]
        faculty = timetable.objects.all().filter(time=obj.time).filter(details="teacher")
        room=classroom.objects.all().filter(room_no=room_no)
        return ({'room':room.values()[0],'faculty':faculty.values(day)[0][day]})
        # ,'throwing_it_out':room_query.values(day)[0][day]})
        # ,'dept':obj.dept_id_id})
        # ,'time' :obj.batch_id_id})
        # 'ishh':now.weekday(),'day':calendar.day_name[now.weekday()]})


# class Meeting_reqSerializer(serializers.ModelSerializer):
    # fac_id = ;
    
    # def get_fac(self,obj):
    #     fac_name = faculties.objects.all().filter(fac_id= fac_id)
    #     return fac_name

    # class Meta:
    #     model = students
    #     fields = ('prn','student_name','dept_id')


