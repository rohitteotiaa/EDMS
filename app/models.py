from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1','MASTERADMIN'),
        ('2','SUPERADMIN'),
        ('3','ADMIN'),
        ('4','USER'),
        
    )
    
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.FileField(upload_to='media/profile_pic')



class Superuser(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=100,default=None)  # Set a default value
    pno_number = models.CharField(max_length=100,default=None) # 77.417998
    address = models.TextField()
    gender = models.CharField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Basicuser(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=100,default=None)  # Set a default value
    pno_number = models.CharField(max_length=100,default=None)
    address = models.TextField()
    gender = models.CharField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Users(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=100,default=None)  # Set a default value
    pno_number = models.CharField(max_length=100,default=None) # 77.417998
    address = models.TextField()
    gender = models.CharField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
    
class contact_us(models.Model):
    subject=models.CharField(max_length=100)
    message=models.TextField()
    

  
  
# class User_message(models.Model):
#     sender = models.CharField(max_length=100)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.sender}: {self.content}' 
    
    #admin models
class superuser_message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
class basicuser_message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}'
    
  
    
class user_message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
  
    
class superuser_admin(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
  
  
    
class superuser_basicuser(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
class superuser_user(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
   
class basicuser_admin(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
class basicuser_superuser(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
class basicuser_user(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
  
      
class user_superuser(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
class user_basicuser(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}' 
    
    
 
 
 
 
    
    
# hitesh


class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    emp_Code = models.CharField(max_length=100, default='None')
    gender = models.CharField(max_length=100, default='None')
    contact = models.CharField(max_length=10, default='None')
    address = models.CharField(max_length=200, default='None')
    working_location = models.CharField(max_length=100, default='None')
    counter = models.ForeignKey('Counter', on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey('zone', on_delete=models.SET_NULL, null=True, blank=True)  # Add a 'zone' field
    section = models.ForeignKey('section', on_delete=models.SET_NULL, null=True, blank=True)  # Add a 'section' field
    room_number = models.ForeignKey('room_number', on_delete=models.CASCADE, null=True, blank=True)
  # Add a 'room_number' field
  
    
    def assign_special_duty(self, area_name):
        # Create a SpecialDuty instance for the selected member
        special_duty = SpecialDuty(member_name=self.name, member_designation=self.designation, area_name=area_name)
        special_duty.save()

        # Remove the member from the Member model
        self.delete()
  



class Counter(models.Model):
    name = models.CharField(max_length=100) 

class zone(models.Model):
    name = models.CharField(max_length=100)

class Duty(models.Model):
    name = models.CharField(max_length=100)

class section(models.Model):
    name=models.CharField(max_length=100)

class room_number(models.Model):
    name=models.CharField(max_length=100)
    

class Assignment(models.Model):
    counter = models.ForeignKey(Counter, on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    room_number = models.ForeignKey(room_number, on_delete=models.CASCADE)


from django.db import models

class AssignmentConfiguration(models.Model):
    zone = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    counter_number = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.zone} - {self.section} - {self.room_number} - Counter {self.counter_number}"

 
class SpecialDuty(models.Model):
    member_name = models.CharField(max_length=100)
    member_designation = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.member_name} - {self.member_designation} - {self.area_name}"



from django.shortcuts import render
from .models import Member, Assignment

def admit_card(request, member_id):
    # Retrieve member details
    member = Member.objects.get(pk=member_id)

    # Retrieve assignment details for the member
    assignments = Assignment.objects.filter(
        zone=member.zone,
        section=member.section,
        room_number=member.room_number,
        counter=member.counter
    )

    # Extract team members' names and designations
    team_members = [
        {'name': assignment.member.name, 'designation': assignment.member.designation}
        for assignment in assignments
    ]

    context = {
        'member': member,
        'assignments': assignments,
        'team_members': team_members,
    }

    return render(request, 'admit_card.html', context)

  

from django.shortcuts import render
from .models import Member, Assignment

def admit_card(request, member_id):
    # Retrieve member details
    member = Member.objects.get(pk=member_id)

    # Retrieve assignment details for the member
    assignments = Assignment.objects.filter(
        zone=member.zone,
        section=member.section,
        room_number=member.room_number,
        counter=member.counter
    )

    # Extract team members' names and designations
    team_members = [
        {'name': assignment.member.name, 'designation': assignment.member.designation}
        for assignment in assignments
    ]

    context = {
        'member': member,
        'assignments': assignments,
        'team_members': team_members,
    }

    return render(request, 'admit_card.html', context)

    