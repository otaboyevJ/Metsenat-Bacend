from django.db import models

# Create your models here.
class Sponsor(models.Model):

    class StatusChoise(models.TextChoices):
        MODERATION = " Moderation ","Moderatsiya"
        NEW = "New","Yangi"
        APPOVED = "Appoved", "Tasdiqlangan"
        CANCELLED = "Cancelled", "Bekor qilingan"

    class TypeChoice(models.TextChoices):
        LEGEL = 'legel', 'yuridik'
        PHYSICAL = 'pyhsical', 'jismoniy'


    class TransactionType(models.TextChoices):
        CASH = 'cash', 'Naqd'
        CARD =  'card', 'Karta'



    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    organization_name = models.CharField(max_length=100,
                                          verbose_name= "Tashkilot nomi",
                                            null = True,
                                              blank = True)
    
    phone_number = models.CharField(max_length=50, verbose_name="Telefon raqami")

    amount = models.PositiveIntegerField(verbose_name="Homiylik summasi ")

    created_at = models.DateField(auto_now_add=True, verbose_name="Ariza sanasi")

    status = models.CharField(max_length=50,
                               choices=StatusChoise.choices,
                                 default=StatusChoise.NEW, verbose_name="Homiyning holati")
    type = models.CharField(max_length=50,
                             choices=TypeChoice.choices,verbose_name="Shahs turi")
    

    transaction_type = models.CharField(max_length=50,
                                         verbose_name="To'lov turi", 
                                         choices=TransactionType.choices,
                                         default=TransactionType.CARD)


    def __str__(self):
        return f"{self.full_name}  {self.phone_number}"

class University(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nomi")

    def __str__(self):
        return self.name


class Student(models.Model):

    class DegreeChoice(models.TextChoices):
        BACHELOR = 'bachelor', 'bakalavor'
        MASTER = 'master', 'magistr'

    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    contract = models.PositiveIntegerField(verbose_name="Kontrakt summasi")
    degree = models.CharField(max_length=50,
                              choices=DegreeChoice.choices,
                              default=DegreeChoice.BACHELOR,
                              verbose_name="Darajasi")
    
    university = models.ForeignKey(University,
                                on_delete=models.SET_NULL,
                                  null=True,
                                    blank=True)





class StudentSponsor(models.Model):
    sponsor  = models.ForeignKey(Sponsor,
               on_delete=models.PROTECT,
                verbose_name="Sponsr",
                related_name="student_sponsor")
    

    student = models.ForeignKey(Student,
            on_delete=models.PROTECT,
            verbose_name="Student",
            related_name="student_sponsor")
    
    amount = models.PositiveIntegerField(verbose_name="Ajratilgan summ")


    def __str__(self):
        return f"{self.sponsor} - {self.student}"
