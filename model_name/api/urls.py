from django.urls import path
from . import views

urlpatterns = [

     path('api/show_classrooms/<status>/', views.Timetable.as_view(),name="show_classrooms"),
     path('api/show_faculty/', views.FacultyList.as_view(),name="show_faculty"),
     path('api/show_faculty/requests', views.Meeting_reqList.as_view(),name="show_faculty_requests"),
     path('api/show_timetable/', views.Timetable.as_view(),name="show_timetable")
     # path('api/show_availability/<status>',views.views.DeptList.as_view(),name = "show_availability")
]
