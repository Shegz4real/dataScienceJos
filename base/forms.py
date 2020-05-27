from django import forms
from .models import ComMember

class MemberForm(forms.ModelForm):
   class Meta:
       model = ComMember
       fields = ('email','name', 'surname','phone' , 'message',)