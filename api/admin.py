from django.contrib import admin

from .models import *






@admin.register(Sponsor)
class Sponsor(admin.ModelAdmin):
    Sponsor = ('id', 'full_name')
    search_fields = ('full_name', )
    list_filter = ('full_name', )

@admin.register(Student)
class Student(admin.ModelAdmin):
    Student = ('id', "full_name")
    search_fields = ('full_name', )
    list_filter = ('full_name', )

@admin.register(University)
class University(admin.ModelAdmin):
    University = ('id', 'full_name')
    search_fields = ('full_name', )
   

@admin.register(StudentSponsor)
class StudentSponsor(admin.ModelAdmin):
    StudentSponsor = ('id', "full_name")
    search_fields = ('full_name', )
    