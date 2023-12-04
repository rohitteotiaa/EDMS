from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
    
admin.site.register(CustomUser,UserModel)
admin.site.register(Superuser)
admin.site.register(Basicuser)
admin.site.register(Users)
admin.site.register(contact_us)
admin.site.register(superuser_basicuser)
admin.site.register(superuser_message)
admin.site.register(basicuser_message)
admin.site.register(user_message)
admin.site.register(superuser_admin)
admin.site.register(superuser_user)
admin.site.register(basicuser_admin)
admin.site.register(basicuser_superuser)
admin.site.register(basicuser_user)
admin.site.register(user_superuser)
admin.site.register(user_basicuser)



# hitesh


admin.site.register(Member)
admin.site.register(Counter)
admin.site.register(Duty)
admin.site.register(Assignment)
admin.site.register(room_number)
admin.site.register(section)
admin.site.register(zone)
admin.site.register(AssignmentConfiguration)
admin.site.register(SpecialDuty)
