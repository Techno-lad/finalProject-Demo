from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, auth





#from .models import Rojay_Beharie_LinearAlgebra_grades
from .models import Rojay_Beharie_CRM_grades
#from .models import Rojay_Beharie_COA_grades
#from .models import Rojay_Beharie_Previous_Modules
#from .models import Nicholas_Pinnock_LinearAlgebra_grades
#from .models import Nicholas_Pinnock_CRM_grades
#from .models import Nicholas_Pinnock_COA_grades
#from .models import Nicholas_Pinnock_Previous_Modules
#from .models import Marvel_Maxwell_LinearAlgebra_grades
#from .models import Marvel_Maxwell_CRM_grades
#from .models import Marvel_Maxwell_COA_grades
#from .models import Marvel_Maxwell_Previous_Modules
#from .models import Kevon_Shakespeare_LinearAlgebra_grades
#from .models import Kevon_Shakespeare_CRM_grades
#from .models import Kevon_Shakespeare_Previous_Modules
#from .models import CRM_Statistics
#from .models import Nicholas_Pinnock_CRM_grades


# Create your views here.


#class UserForm(forms.Form,):
    #favorite_fruit= forms.CharField(label='Which module would you like to view?', widget=forms.Select(choices=MODULE_CHOICES))
  

class studDashbrdView(TemplateView):
    template_name='rojayDash.html'
       
    def get_context_data(self, **kwargs): 
          context = super().get_context_data(**kwargs)
          context["qs"] = Rojay_Beharie_CRM_grades.objects.all()
          return context


     # def decision(self,request):
      #    if request.method == 'POST' and studDashbrd.forms.ChoiceField == 'Crm' :
       #     return True
      #    else: 
       #     return False 

    
   

    

  

