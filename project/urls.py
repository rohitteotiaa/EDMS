"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,admin_views,superuser_views,basicuser_views,user_views
from .views import*

urlpatterns = [
    #views
    
    path('admin/', admin.site.urls),
    path("",index,name='login'),
    path("dologin",views.dologin,name='dologin'),
    path("dologout",views.dologout,name='logout'),
    


    # admin
    path("home/",admin_views.home,name='admin_home'),
    path("home/basic-form/",admin_views.basic,name='basic'),
    path("home/view-superuser/",admin_views.view_superuser,name='viewsuperuser'),
    path("home/view-basicuser/",admin_views.view_basicuser,name='viewbasicuser'),
    path("home/view-user/",admin_views.view_user,name='viewuser'),
    path("home/add-superuser/",admin_views.addsuperuser,name='addsuperuser'),
    path("home/add-basicuser/",admin_views.addbasicuser,name='addbasicuser'),
    # path("home/basicuser/edit/<str:id>",admin_views.edit_user,name='edituser'),
    path("home/basicuser/edit/<str:id>",admin_views.edit_basicuser,name='editbasicuser'),
    path("home/superuser/edit/<str:id>",admin_views.edit_superuser,name='editsuperuser'),
    path("home/superuser/update/",admin_views.update_superuser,name='update_superuser'),
    path("home/basicuser/update/",admin_views.update_basicuser,name='update_basicuser'),
    path("home/basicuser/delete/<str:admin>",admin_views.delete_basicuser,name='delete_basicuser'),
    path("home/superuser/delete/<str:admin>",admin_views.delete_superuser,name='delete_superuser'),
    path("home/view-basicuser/download-pdf/",admin_views.download_basicuser,name='basicuser-download-pdf'),
    path("home/view-superuserdownload-pdf/",admin_views.download_superuser,name='superuser-download-pdf'),
    path("home/view-user/download-pdf/",admin_views.download_user,name='user-download-pdf'),
    path('home/broadcast/message_sent/',admin_views.message_sent_admin, name='message_sent_admin'),
    path('home/broadcast-message/superuser/', admin_views.send_message_superuser, name='send_message_superuser'),
    path('home/broadcast-message/basicuser/', admin_views.send_message_basicuser, name='send_message_basicuser'),
    path('home/broadcast-message/users/', admin_views.send_message_user, name='send_message_user'),
    path('home/broadcast-message/message-from-superuser/',admin_views.message_from_superuser,name = 'message-from-superuser'),
    path('home/broadcast-message/message-from-basicuser/',admin_views.message_from_basicuser,name = 'message-from-basicuser'),
    
    
    # hitesh
    path('home/assign/', admin_views.assignment_page, name='assignment_page'),
    path('home/assigned-data/dashboard/', admin_views.dashboard, name='dashboard'),
    path('home/upload-file/upload/',admin_views.upload_csv, name= 'upload_csv'),
    path('home/upload-file/upload_post/',admin_views.upload_post, name= 'upload_post'),
    path("home/final-report/download-pdf/",admin_views.download_dashboard,name='download_dashboard'),
    
    path('home/unassign_and_assign_special_duty/', admin_views.unassign_and_assign_special_duty, name='unassign_and_assign_special_duty'),
    path('home/unassign_teamleader_special_duty/', admin_views.unassign_teamleader_special_duty, name='unassign_teamleader_special_duty'),
    path('home/unassign_clerk_special_duty/', admin_views.unassign_clerk_special_duty, name='unassign_clerk_special_duty'),
    path('home/special_duty_view/',admin_views.special_duty_view,name='special_duty_view'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    #superuser

    path("home/superuser/dashboard",superuser_views.home2,name='superuser_home2'), 
    path("home/superuser/advance-form/",superuser_views.advance2,name='advance2'),
    path("home/superuser/view-user/",superuser_views.view_user2,name='viewuser2'),
    path("home/superuser/view-basicuser/",superuser_views.view_basicuser2,name='viewbasicuser2'),
    path("home/superuser/add-customuser/",superuser_views.adduser2,name='addcustomuser2'),
    path("home/superuser/add-basicuser/",superuser_views.addbasicuser2,name='addbasicuser2'),
    path("home/superuser/user/edit/<str:id>",superuser_views.edit_user2,name='edituser2'),
    path("home/superuser/basiuser/edit/<str:id>",superuser_views.edit_basicuser2,name='editbasicuser2'),
    path("home/superuser/user/update/",superuser_views.update_user2,name='update_user2'),
    path("home/superuser/basicuser/update/",superuser_views.update_basicuser2,name='update_basicuser2'),

    path("home/superuser/basicuser/delete/<str:admin>",superuser_views.delete_basicuser2,name='delete_basicuser2'),
    path("home/superuser/user/delete/<str:admin>",superuser_views.delete_user2,name='delete_user2'),
    path("home/superuser/view-basicuser/download-pdf/",superuser_views.download_basicuser2,name='basicuser-download-pdf2'),
    path("home/superuser/view-user/download-pdf/",superuser_views.download_user2,name='user-download-pdf2'),

    
    path('home/superuser/broadcast/message_sent/',superuser_views.message_sent, name='message_sent'),

    path('home/superuser/broadcast-message/message-from-admin/', superuser_views.message_from_admin, name='message_from_admin'),
    path('home/superuser/broadcast-message/message-from-basicuser/', superuser_views.message_from_basicuser, name='message_from_basicuser2'),
    path('home/superuser/broadcast-message/message-from-user/', superuser_views.message_from_user, name='message_from_user2'),
    path('home/superuser/broadcast-message/master/', superuser_views.send_message_admin, name='send_message_admin2'),
    path('home/superuser/broadcast-message/basicuser/', superuser_views.send_message_basicuser, name='send_message_basicuser2'),
    path('home/superuser/broadcast-message/users/', superuser_views.send_message_user, name='send_message_user2'),
    




    # hitesh
    path('home/superuser/assign-data/', superuser_views.assignment_page2, name='assignment_page2'),
    path('home/superuser/assigned-data/dashboard/', superuser_views.dashboard2, name='dashboard2'),
    path('home/superuser/upload-file/upload-emp/',superuser_views.upload_csv2, name= 'upload_csv2'),
    path('home/superuser/upload-file/upload_post/',superuser_views.upload_post2, name= 'upload_post2'),
    path("home/superuser/final-report/download-pdf/",superuser_views.download_dashboard2,name='download_dashboard2'),

    path('home/superuser/unassign_and_assign_special_duty/', superuser_views.unassign_and_assign_special_duty2, name='unassign_and_assign_special_duty2'),
    path('home/superuser/unassign_teamleader_special_duty/', superuser_views.unassign_teamleader_special_duty2, name='unassign_teamleader_special_duty2'),
    path('home/superuser/unassign_clerk_special_duty/', superuser_views.unassign_clerk_special_duty2, name='unassign_clerk_special_duty2'),
    path('home/superuser/special_duty_view/',superuser_views.special_duty_view2,name='special_duty_view2'),




    

    #basicuser
    path("home/basicuser/dashboard",basicuser_views.home3,name='basicuser_home3'), 
    path("home/basicuser/view-user/",basicuser_views.view_user3,name='viewuser3'),
    path("home/basicuser/add-customuser/",basicuser_views.adduser3,name='addcustomuser3'),
    path("home/basicuser/view-user/download-pdf/",basicuser_views.download_user3,name='user-download-pdf3'),
    path("home/basicuser/user/delete/<str:admin>",basicuser_views.delete_user3,name='delete_user3'),
    path("home/basicuser/user/update/",basicuser_views.update_user3,name='update_user3'),
    path("home/basicuser/user/edit/<str:id>",basicuser_views.edit_user3,name='edituser3'),
    
    path('home/basicuser/broadcast-message/message-from-admin/', basicuser_views.message_from_admin3, name='message_from_admin3'),
    path('home/basicuser/broadcast-message/message-from-superuser/', basicuser_views.message_from_superuser3, name='message_from_superuser3'),
    path('home/basicuser/broadcast-message/message-from-user/', basicuser_views.message_from_user3, name='message_from_user3'),
    path('home/basicuser/broadcast-message/message-to-admin/', basicuser_views.send_message_admin3, name='message_to_admin3'),
    path('home/basicuser/broadcast-message/message_sent/', basicuser_views.message_sent_basicuser3, name='message_sent_basicuser'),
    path('home/basicuser/broadcast-message/message-to-superuser/', basicuser_views.send_message_superuser3, name='message_to_superuser3'),
    path('home/basicuser/broadcast-message/message-to-user/', basicuser_views.send_message_user3, name='message_to_user3'),
    
    
    
    # hitesh
    path('home/basicuser/assign-data/', basicuser_views.assignment_page3, name='assignment_page3'),
    path('home/basicuser/assigned-data/dashboard/', basicuser_views.dashboard3, name='dashboard3'),
    path('home/basicuser/upload-file/upload-emp/',basicuser_views.upload_csv3, name= 'upload_csv3'),
    path('home/basicuser/upload-file/upload_post/',basicuser_views.upload_post3, name= 'upload_post3'),
    
    
    path('home/basicuser/unassign_and_assign_special_duty/', basicuser_views.unassign_and_assign_special_duty3, name='unassign_and_assign_special_duty3'),
    path('home/basicuser/unassign_teamleader_special_duty/', basicuser_views.unassign_teamleader_special_duty3, name='unassign_teamleader_special_duty3'),
    path('home/basicuser/unassign_clerk_special_duty/', basicuser_views.unassign_clerk_special_duty3, name='unassign_clerk_special_duty3'),
    path('home/basicuser/special_duty_view/',basicuser_views.special_duty_view3,name='special_duty_view3'),
    
    
    
    
    #users
    path("home/users/dashboard/",user_views.home4,name='user_home4'),
    
    path("home/users/vehicle_alloted/",user_views.vehicle_alloted,name='vehicle_alloted'),
    path("home/users/download_id_card/<int:member_id>/",user_views.admit_card,name='admit_card'),
    
    path("home/users/download_id_card_search/",user_views.admit_card_search,name='admit_card_search'),
    
    path("home/users/id_card/download-pdf/",user_views.download_id_card_download,name='download_id_card_download'),
    
    path('home/users/broadcast-message/message-from-admin/', user_views.message_from_admin, name='message_from_admin4'),
    path('home/users/broadcast-message/message-from-superuser/', user_views.message_from_superuser, name='message_from_superuser4'),
    path('home/users/broadcast-message/message-from-basicuser/', user_views.message_from_basicuser, name='message_from_basicuser4'),
    
    path('home/users/broadcast-message/message_sent/', user_views.message_sent_user, name='message_sent_user'),
    path('home/users/broadcast-message/message-to-superuser/', user_views.send_message_superuser, name='message_to_superuser4'),
    path('home/users/broadcast-message/message-to-basicuser/', user_views.send_message_basicuser, name='message_to_basicuser4'),
    
    
    path('login/', user_views.admit_card_access, name='admit_card_access'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
