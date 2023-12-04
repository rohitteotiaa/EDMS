from django import forms
# from .models import Message
from .models import *




# class SendMessageFormuser(forms.ModelForm):
#     class Meta:
#         model = User_message
#         fields = ['sender', 'content']
        
class SendMessageFormsuperuser(forms.ModelForm):
    class Meta:
        model = superuser_message
        fields = ['sender', 'content']
        
        
class SendMessageFormbasicuser(forms.ModelForm):
    class Meta:
        model = basicuser_message
        fields = ['sender', 'content']
        
class SendMessageFormusers(forms.ModelForm):
    class Meta:
        model = user_message
        fields = ['sender', 'content']
        
        
class superuser_to_admin(forms.ModelForm):
    class Meta:
        model = superuser_admin
        fields = ['sender', 'content']
        
        
class superuser_to_basicuser(forms.ModelForm):
    class Meta:
        model = superuser_basicuser
        fields = ['sender', 'content']
        

class superuser_to_user(forms.ModelForm):
    class Meta:
        model = superuser_user
        fields = ['sender', 'content']
        
      
class basicuser_to_admin(forms.ModelForm):
    class Meta:
        model = basicuser_admin
        fields = ['sender', 'content']   
        
        
class basicuser_to_superuser(forms.ModelForm):
    class Meta:
        model = basicuser_superuser
        fields = ['sender', 'content']  
        
        
class basicuser_to_user(forms.ModelForm):
    class Meta:
        model = basicuser_user
        fields = ['sender', 'content']     
        
  
    
        
        
class user_to_superuser(forms.ModelForm):
    class Meta:
        model = user_superuser
        fields = ['sender', 'content']  
        
        
class user_to_basicuser(forms.ModelForm):
    class Meta:
        model = user_basicuser
        fields = ['sender', 'content'] 
        
        
        
        
# hitesh



class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


class CSVUploadpost(forms.Form):
    csv_file = forms.FileField()    
        
        
 
 
class SpecialDutyAssignmentForm(forms.Form):
    managers = forms.ModelMultipleChoiceField(
        queryset=Member.objects.filter(designation='Manager', counter=None),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    area_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))

class SpecialDutyAssignmentForm1(forms.Form):
    team_leaders = forms.ModelMultipleChoiceField(
        queryset=Member.objects.filter(designation='Team Leader', counter=None),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    area_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))


class SpecialDutyAssignmentForm2(forms.Form):
    clerk= forms.ModelMultipleChoiceField(
        queryset=Member.objects.filter(designation='Clerk', counter=None),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    area_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        