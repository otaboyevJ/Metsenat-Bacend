from rest_framework import serializers 
from . import models
from django.db.models import Sum

class SponserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        fields = (
            'id',
            'full_name',
            'phone_number',
            'organization_name',
            'amount',
            'type'
        )
        extra_kwargs = {
            "id" : {
                "read_only":True
            }
        }

    #attrs = {
    #     'type': 'legal',
    #    'organization': ...,  
    # }

    def validate(self, attr):
        type = attr.get("type") 
        org_name = attr.get("organization_name")
        
        #type == "pyhsical"
        # a
        if type == "pyhsical" and org_name:
            raise serializers.ValidationError(detail={
                "error": "Jismoniy shaxs orginizatiya to'ldirishi mumkin emas"
            })


        if type == "legel" and not org_name:
            raise serializers.ValidationError(detail={
                "error": "Yuridik shaxs orginizatiya to'ldirishi kerak"
            })


        return attr

class SponsorListSerializers(serializers.ModelSerializer):
    sponsor_amount = serializers.SerializerMethodField()

    def get_sponsor_amount(self, obj):
        a = obj.student_sponsor.aggregate(Sum('amount'))
        return a['amount__sum'] if a['amount__sum'] else 0


    class Meta:
        model = models.Sponsor
        fields = (
            "id",
            "full_name",
            "phone_number",
            "amount",
            "created_at",
            "status",
            "sponsor_amount"
            
        )
        
        extra_kwargs = {
            "id" : {
                "read_only":True
            }
        }

class SponsorUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        fields = "__all__"


class SponsorStudentCreateAPIView(serializers.ModelSerializer):


    class Meta:
        model = models.StudentSponsor
        fields = "__all__"

    def create(self, validated_data):
        amount = validated_data.get("amount")
        student = validated_data.get("student")
        sponsor = validated_data.get("sponsor")

        totol_amount = sum(models.StudentSponsor.objects.filter(student=student).values_list("amount", flat=True))
        
        #student =  models.Student.objects.get(id=student)
        if totol_amount + amount > student.contract:
            raise serializers.ValidationError(detail={
                "error": "Siz ko'pi bilan{student.contract - total_amount} pul qo'sha olasiz"
            })
             

        return super().create(validated_data)




class StudentListSerializer(serializers.ModelSerializer):
    student_amount = serializers.SerializerMethodField(method_name="total_student_amount")

    def total_student_amount(self, obj):
        result = models.StudentSponsor.objects.filter(student=obj).values_list('amount', flat=True)
        return result
   
    class Meta:
        model = models.Student
        fields = ("id",
            "full_name",
            "contract",
            "degree",
            "university",
            "student_amount"
                  )



class StudentDetailSerializer(serializers.ModelSerializer):
    student_amount = serializers.SerializerMethodField(method_name="total_student_amount")

    def total_student_amount(self, obj):
        result = models.StudentSponsor.objects.filter(student=obj).values_list('amount', flat=True)
        return result
    
    class Meta:
        model = models.Student
        fields = ("id",
            "full_name",
            "contract",
            "degree",
            "university",
            "student_amount"
                  )

#class StudentUpdateSerizalizer(serializers.ModelSerializer):
    #student_amount = serializers.SerializerMethodField(method_name= "")




