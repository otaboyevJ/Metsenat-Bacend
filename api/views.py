from msilib.schema import RadioButton
from tracemalloc import start
from unittest import result
from django.shortcuts import render
from . import serializers, models
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView, Response
from django.db.models import Sum
from .models import StudentSponsor, Student
import calendar


class SponsorCreateAPIView(CreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponserCreateSerializer

class SponsorListApiView(ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializers
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ("full_name",)
    filterset_fields = ("created_at", 'status', 'amount')

class SponsorRetriveApiView(RetrieveAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorListSerializers

class SponsorUpdateAPIView(UpdateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorUpdateSerializers


class SponsorStudentCreateAPIView(CreateAPIView):
    queryset = models.StudentSponsor.objects.all()
    serializer_class = serializers.SponsorStudentCreateAPIView

class StudentListAPIView(ListAPIView):
    queryset = models. Student.objects.all()
    serializer_class = serializers.StudentListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_filter = {"full_name"}
    filterset_fields = {"degree", "university"}


class DeshportStatisticAPIView(APIView):
    

    def get(self,request):

        total_paid_money = StudentSponsor.objects.aggregate(Sum("amount"))['amount__sum']

        total_contract = Student.objects.aggregate(Sum("contract"))['contract__sum']

        return Response({
            "total_paid_money": total_paid_money,
            "total_contract": total_contract,
            #"total_left_money": total_contract - total_paid_money
        })

class StudentDetailAPIView(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentDetailSerializer

class GrafikAPIView(APIView):
    
    def get(self, request):
        from datetime import date, timedelta
        this_year = date.today().year
        start_date = date(this_year, month=1, day=1)
        end_date = date(this_year, month=12, day=31)

        result = []

        while start_date < end_date:
            this_month = start_date.month
            this_year = start_date.year
            num_days=calendar.monthrange(this_year, this_month)[1]
            this_days = calendar.monthrange(this_year, this_month)[1]
            queryset = models.Sponsor.objects.filter(created_at__range
                                                     =(start_date, date(this_year,this_month,num_days))).count()
            
            result.append({
                "month":start_date.strftime('%B'),
                "sponsor_count": queryset,
            })
            start_date += timedelta(days=num_days)

        return Response(result)