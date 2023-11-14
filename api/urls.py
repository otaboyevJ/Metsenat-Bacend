from django.urls import path
from . import views


urlpatterns = [
    path("sponsor-create/", views.SponsorCreateAPIView.as_view()),
    path("list-sponsor/", views.SponsorListApiView.as_view()),
    path("retrive-sponsor/<int:pk>/", views.SponsorRetriveApiView.as_view()),
    path("sponsor-update/<int:pk>/", views.SponsorUpdateAPIView.as_view()),
    path("student-sponsor/", views.SponsorStudentCreateAPIView.as_view()),
    path("student-listapi/", views.StudentListAPIView.as_view()),
    path("deshport-statistik/", views.DeshportStatisticAPIView.as_view()),
    path("student-detail/<int:pk>/", views.StudentDetailAPIView.as_view()),
    path("deshboard-garfik/", views.GrafikAPIView.as_view())
]
