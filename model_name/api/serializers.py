from datetime import date
from distutils.command.clean import clean
from rest_framework import serializers
from model_name.models import classroom, timetable
from datetime import datetime
import calendar

# class MyProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MyProduct
#         fields = ('id',
#                   'name',
#                   'product_code',
#                   'visibility',
#                   'currency_type',
#                   'price',
#                   'requester_ip',
#                   'created_date')

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = ('room_no', 'status', 'course_id', 'capacity', 'projector',
                  'ac', 'computer', 'desks', 'whiteboard', 'count', 'type')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields=('fac_id','fac_name','dept_id','fac_role')

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
