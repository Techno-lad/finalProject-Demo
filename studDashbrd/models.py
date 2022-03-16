from django.db import models

# Create your models here.

#Rojay CRM module model


class Rojay_Beharie_CRM_grades(models.Model): 
    
    assesment = models.CharField(max_length=100, primary_key=True)
    gradePercentage = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.assesment, self.gradePercentage)


