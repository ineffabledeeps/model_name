from django.urls import path
from . import views

urlpatterns = [

     path('api/show_classrooms/<status>/', views.Timetable.as_view(),name="show_classrooms"),
     path('api/show_faculty/', views.FacultyList.as_view(),name="show_faculty"),
     path('api/send_requests/', views.Send_meeting_reqList.as_view(),name="sendMeetingRequests"),
     path('api/get_requests/', views.Get_meeting_reqList.as_view(),name="getRequests"),
     path('api/get_requests/set/', views.Set_reqList.as_view(),name="Set Requests"),
     path('api/show_timetable/', views.Timetable.as_view(),name="show_timetable")
     # path('api/show_availability/<status>',views.views.DeptList.as_view(),name = "show_availability")
]
