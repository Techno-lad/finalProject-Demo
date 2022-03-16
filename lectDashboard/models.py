from django.db import models

# Create your models here.
class David_Wright_CRM_Class(models.Model): 
    
    student = models.CharField(max_length=100, primary_key=True)
    test1 = models.IntegerField()
    test2 = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.student, self.test1, self.test2)