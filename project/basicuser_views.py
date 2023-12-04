from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
import json
from django.core.paginator import Paginator
import pdfkit

from django.core.paginator import Paginator
import pdfkit
from django.template.loader import get_template
from xhtml2pdf import pisa
from app.forms import *
from app.models import *


@login_required(login_url='/')
def home3(request):
    if request.method == "POST":
        contact = contact_us(
            
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
        
    contact = contact_us.objects.all()   
    
    return render(request,'basicuser/home3.html')   
    



@login_required(login_url='/')
def adduser3(request):
    
    if request.method == "POST":
        # profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        contact_number = request.POST.get('contact_number')
        pno_number = request.POST.get('pno_number')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Is Already Teken")
            return redirect('addcustomuser3')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"Username Is Already Teken")
            return redirect('addcustomuser3')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name= last_name,
                email=email,
                username=username,
                # profile_pic = profile_pic,
                user_type = 4,
            )
            user.set_password(password)
            user.save()
            
            employee = Users(
                admin = user,
                contact_number=contact_number,
                pno_number=pno_number,
                address = address,
                gender = gender,
                
                
            )
            employee.save()
            messages.success(request,'Employee Successfully Saved')
            return redirect('addcustomuser3')
            
    return render(request,'basicuser/adduser3.html')





@login_required(login_url='/')

def view_user3(request):
    users = Users.objects.all()
    
    items_per_page = 10
    paginator = Paginator(users, items_per_page)
    
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    context = {
        'users' : users,
    }
    
    return render(request,'basicuser/viewuser3.html',context)



def download_user3(request):
    user = Users.objects.all()
    
    template_path = 'basicuser/view_download_user3.html'
    context = {'user': user}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




    

    



def delete_user3(request,admin):
    user=CustomUser.objects.get(id = admin)
    user.delete()
    messages.success(request,"Record Are Successfully Deleted !")
    return redirect('viewuser3')




def edit_user3(request,id):
    users=Users.objects.filter(id = id)
    context = {
        'users':users
    }
    return render(request,'basicuser/edit_user3.html',context)



def update_user3(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        contact_number = request.POST.get('contact_number')
        pno_number = request.POST.get('pno_number')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        users =CustomUser.objects.get(id = user_id)
        users.first_name=first_name
        users.last_name=last_name
        users.email=email
        users.username=username
        
        if password != None and password != "":
            users.set_password(password)
            
        users.save()
        
        customuser=Users.objects.get(admin = user_id)
        customuser.address=address
        customuser.gender=gender
        customuser.contact_number=contact_number
        customuser.pno_number=pno_number
        
        customuser.save()
        messages.success(request,'Record Are Successfully Updated !')
        redirect('viewuser3')
        
    return render(request,'basicuser/edit_user3.html')



def message_from_admin3(request):
    messages = basicuser_message.objects.all().order_by('-timestamp')
    return render(request, 'basicuser/message_from_admin3.html', {'messages': messages})


def message_from_superuser3(request):
    messages = superuser_basicuser.objects.all().order_by('-timestamp')
    return render(request, 'basicuser/message_from_superuser3.html', {'messages': messages})


def message_from_user3(request):
    messages = user_basicuser.objects.all().order_by('-timestamp')
    return render(request, 'basicuser/message_from_user3.html', {'messages': messages})


def message_sent_basicuser3(request):
    return render (request,'basicuser/message_sent_basicuser.html')


def send_message_admin3(request):
    if request.method == 'POST':
        form = basicuser_to_admin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent_basicuser')
    else:
        form = basicuser_to_admin()
    return render(request, 'basicuser/message_to_admin3.html', {'form': form})


def send_message_superuser3(request):
    if request.method == 'POST':
        form = basicuser_to_superuser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent_basicuser')
    else:
        form = basicuser_to_superuser()
    return render(request, 'basicuser/message_to_superuser3.html', {'form': form})



def send_message_user3(request):
    if request.method == 'POST':
        form = basicuser_to_user(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent_basicuser')
    else:
        form = basicuser_to_user()
    return render(request, 'basicuser/message_to_user3.html', {'form': form})







# hitesh


import pandas as pd
# from app.forms import 
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *

from django.db import transaction

# ...

@transaction.atomic
def assignment_page3(request):
    if request.method == "POST":
        assignment_type = request.POST.get("assignment-type")

        if assignment_type == "manual":
            # Handle manual assignment logic
            zone_value = request.POST.get("zone")
            section_value = request.POST.get("section")
            room_number_value = request.POST.get("room_number")
            counter_id = request.POST.get("counter")

            zone_instance = zone.objects.get(name=zone_value)
            section_instance = section.objects.get(name=section_value)
            room_number_instance = room_number.objects.get(name=room_number_value)

            counter_config = {
                '1': {'managers': 1, 'team_leaders': 2, 'clerk': 4},
                '2': {'managers': 1, 'team_leaders': 2, 'clerk': 4},
                '3': {'managers': 1, 'team_leaders': 3, 'clerk': 6},
                '4': {'managers': 1, 'team_leaders': 3, 'clerk': 6},
                '5': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                '6': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                '7': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                '8': {'managers': 3, 'team_leaders': 8, 'clerk': 20},
                '9': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                '10': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                '11': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                '12': {'managers': 5, 'team_leaders': 12, 'clerk': 20},
                '13': {'managers': 5, 'team_leaders': 12, 'clerk': 20},
            }
            if counter_id not in counter_config:
                return redirect('assignment_page3')

            counter = Counter.objects.get(pk=counter_id)
            managers_to_assign = counter_config[counter_id]['managers']
            team_leaders_to_assign = counter_config[counter_id]['team_leaders']
            clerk_to_assign = counter_config[counter_id]['clerk']

            managers = Member.objects.filter(designation="Manager", counter=None)
            team_leaders = Member.objects.filter(designation="Team Leader", counter=None)
            clerk = Member.objects.filter(designation="Clerk", counter=None)
            
            if len(managers) < managers_to_assign or len(team_leaders) < team_leaders_to_assign or len(clerk) < clerk_to_assign:
                return redirect('assignment_page3')
            
            assigned_managers = random.sample(list(managers), managers_to_assign)
            assigned_team_leaders = random.sample(list(team_leaders), team_leaders_to_assign)
            assigned_clerk = random.sample(list(clerk), clerk_to_assign)

            for manager in assigned_managers:
                manager.counter = counter
                manager.room_number = room_number_instance
                manager.section = section_instance
                manager.zone = zone_instance
                manager.save()
                assignment = Assignment(
                    counter=counter, duty=Duty.objects.get(name="Manager"), member=manager,
                    room_number=room_number_instance, section=section_instance, zone=zone_instance
                )
                assignment.save()

            for team_leader in assigned_team_leaders:
                team_leader.counter = counter
                team_leader.room_number = room_number_instance
                team_leader.section = section_instance
                team_leader.zone = zone_instance
                team_leader.save()
                assignment = Assignment(
                    counter=counter, duty=Duty.objects.get(name="Team Leader"), member=team_leader,
                    room_number=room_number_instance, section=section_instance, zone=zone_instance
                )
                assignment.save()

            for clerk in assigned_clerk:
                clerk.counter = counter
                clerk.room_number = room_number_instance
                clerk.section = section_instance
                clerk.zone = zone_instance
                clerk.save()
                assignment = Assignment(
                    counter=counter, duty=Duty.objects.get(name="Clerk"), member=clerk,
                    room_number=room_number_instance, section=section_instance, zone=zone_instance
                )
                assignment.save()




        elif assignment_type == "automatic":
            # Handle automatic assignment logic
            assignment_configurations = AssignmentConfiguration.objects.all()

            for assignment_configuration in assignment_configurations:
                zone_instance = zone.objects.get(name=assignment_configuration.zone)
                section_instance = section.objects.get(name=assignment_configuration.section)
                room_number_instance = room_number.objects.get(name=assignment_configuration.room_number)
                counter_id = assignment_configuration.counter_number

            
                counter_config = {
                    '1': {'managers': 1, 'team_leaders': 2, 'clerk': 4},
                    '2': {'managers': 1, 'team_leaders': 2, 'clerk': 4},
                    '3': {'managers': 1, 'team_leaders': 3, 'clerk': 6},
                    '4': {'managers': 1, 'team_leaders': 3, 'clerk': 6},
                    '5': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                    '6': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                    '7': {'managers': 2, 'team_leaders': 5, 'clerk': 10},
                    '8': {'managers': 3, 'team_leaders': 8, 'clerk': 20},
                    '9': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                    '10': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                    '11': {'managers': 4, 'team_leaders': 10, 'clerk': 25},
                    '12': {'managers': 5, 'team_leaders': 12, 'clerk': 20},
                    '13': {'managers': 5, 'team_leaders': 12, 'clerk': 20},
                }

                if counter_id not in counter_config:
                    continue  

                counter = Counter.objects.get(pk=counter_id)
                managers_to_assign = counter_config[counter_id]['managers']
                team_leaders_to_assign = counter_config[counter_id]['team_leaders']
                clerk_to_assign = counter_config[counter_id]['clerk']

                managers = Member.objects.filter(designation="Manager", counter=None)
                team_leaders = Member.objects.filter(designation="Team Leader", counter=None)
                clerk = Member.objects.filter(designation="Clerk", counter=None)

                if len(managers) < managers_to_assign or len(team_leaders) < team_leaders_to_assign or len(clerk) < clerk_to_assign:
                    continue  

                assigned_managers = random.sample(list(managers), managers_to_assign)
                assigned_team_leaders = random.sample(list(team_leaders), team_leaders_to_assign)
                assigned_clerk = random.sample(list(clerk), clerk_to_assign)

                for manager in assigned_managers:
                    manager.counter = counter
                    manager.room_number = room_number_instance
                    manager.section = section_instance
                    manager.zone = zone_instance
                    manager.save()
                    assignment = Assignment(
                        counter=counter, duty=Duty.objects.get(name="Manager"), member=manager,
                        room_number=room_number_instance, section=section_instance, zone=zone_instance
                    )
                    assignment.save()

                for team_leader in assigned_team_leaders:
                    team_leader.counter = counter
                    team_leader.room_number = room_number_instance
                    team_leader.section = section_instance
                    team_leader.zone = zone_instance
                    team_leader.save()
                    assignment = Assignment(
                        counter=counter, duty=Duty.objects.get(name="Team Leader"), member=team_leader,
                        room_number=room_number_instance, section=section_instance, zone=zone_instance
                    )
                    assignment.save()

                for clerk in assigned_clerk:
                    clerk.counter = counter
                    clerk.room_number = room_number_instance
                    clerk.section = section_instance
                    clerk.zone = zone_instance
                    clerk.save()
                    assignment = Assignment(
                        counter=counter, duty=Duty.objects.get(name="Clerk"), member=clerk,
                        room_number=room_number_instance, section=section_instance, zone=zone_instance
                    )
                    assignment.save()

            AssignmentConfiguration.objects.all().delete()

        else:
            return redirect('assignment_page3')


        return redirect('dashboard3')

    counters = Counter.objects.all()
    available_sections = section.objects.all()
    available_zone = zone.objects.all()
    available_room = room_number.objects.all()
    available_counter = Counter.objects.all()
    return render(request, 'basicuser/assignment_page3.html', {'counters': counters, 'available_sections': available_sections, 'available_zone': available_zone, 'available_room': available_room, 'available_counter': available_counter })


def dashboard3(request):
    zones = zone.objects.all()
    sections = section.objects.all()
    rooms = room_number.objects.all()
    counters = Counter.objects.all()

    data = []

    for zone_instance in zones:
        for room in rooms:
            for counter in counters:
                for section_instance in sections:
                    assigned_members = Assignment.objects.filter(
                        zone=zone_instance,
                        section=section_instance,
                        room_number=room,
                        counter=counter
                    ).select_related('member')

                    if assigned_members:
                        data.append({
                            'zone': zone_instance,
                            'section': section_instance,
                            'room': room,
                            'counter': counter,
                            'assigned_members': assigned_members
                        })

    unassigned_managers = Member.objects.filter(designation="Manager", counter=None).count()
    unassigned_team_leaders = Member.objects.filter(designation="Team Leader", counter=None).count()
    unassigned_clerk = Member.objects.filter(designation="Clerk", counter=None).count()

    return render(request, 'basicuser/dashboard3.html', {
        'data': data,
        'unassigned_managers': unassigned_managers,
        'unassigned_team_leaders': unassigned_team_leaders,
        'unassigned_clerk': unassigned_clerk
    })



def upload_csv3(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['csv_file']


            if uploaded_file.name.endswith(('.csv', '.xlsx')):
                try:
                    if uploaded_file.name.endswith('.csv'):
                        data = pd.read_csv(uploaded_file)
                    elif uploaded_file.name.endswith('.xlsx'):
                        data = pd.read_excel(uploaded_file)

                
                    for _, row in data.iterrows():
                        member = Member(
                            name=row['Name'],
                            designation=row['Designation'],
                            emp_Code=row['Emp Code'],
                            gender=row['Gender'],
                            contact=row['Mobile No.'],
                            address=row['Personal Address'],
                            working_location=row['Working Location']
                        )
                        member.save()

                    return HttpResponse('File uploaded and data inserted into the database.')

                except Exception as e:
                    return HttpResponse(f'An error occurred: {str(e)}')
            else:
                return HttpResponse('Unsupported file type. Please upload a CSV or Excel file.')

    else:
        form = CSVUploadForm()

    return render(request, 'basicuser/upload_file3.html', {'form': form})


def upload_post3(request):
    if request.method == 'POST':
        form = CSVUploadpost(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['csv_file']


            if uploaded_file.name.endswith(('.csv', '.xlsx')):
                try:
                    if uploaded_file.name.endswith('.csv'):
                        data = pd.read_csv(uploaded_file)
                    elif uploaded_file.name.endswith('.xlsx'):
                        data = pd.read_excel(uploaded_file)

                
                    for _, row in data.iterrows():
                        post = AssignmentConfiguration(
                            zone=row['Zone'],
                            section=row['Section'],
                            room_number=row['Room Number'],
                            counter_number=row['Counter Number'],
                        )
                        post.save()

                    return HttpResponse('File uploaded and data inserted into the database.')

                except Exception as e:
                    return HttpResponse(f'An error occurred: {str(e)}')
            else:
                return HttpResponse('Unsupported file type. Please upload a CSV or Excel file.')

    else:
        form = CSVUploadpost()

    return render(request, 'basicuser/upload_post3.html', {'form': form})





def unassign_and_assign_special_duty3(request):
    form = SpecialDutyAssignmentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Handle form submission to unassign and assign special duty
        selected_managers = form.cleaned_data['managers']
        area_name = form.cleaned_data['area_name']

        # Create SpecialDuty instances for selected managers
        for manager in selected_managers:
            manager.assign_special_duty(area_name)

        # Redirect to the special duty page with the assigned members
        assigned_members = SpecialDuty.objects.filter(area_name=area_name)
        return render(request, 'basicuser/special_duty.html', {'assigned_members': assigned_members, 'area_name': area_name})

    # If the request method is not POST or the form is invalid, render the dashboard
    counters = Counter.objects.all()
    available_sections = section.objects.all()
    available_zone = zone.objects.all()
    available_room = room_number.objects.all()
    available_counter = Counter.objects.all()
    
    # Add the form to the context
    context = {
        'counters': counters,
        'available_sections': available_sections,
        'available_zone': available_zone,
        'available_room': available_room,
        'available_counter': available_counter,
        'form': form,
    }

    return render(request, 'basicuser/assign_manager.html', context)


# views.py
from django.shortcuts import render
from app.models import SpecialDuty

def unassign_teamleader_special_duty3(request):
    form = SpecialDutyAssignmentForm1(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Handle form submission to unassign and assign special duty
        selected_team_leader = form.cleaned_data['team_leaders']
        area_name = form.cleaned_data['area_name']

        # Create SpecialDuty instances for selected team leaders
        for team_leader in selected_team_leader:
            team_leader.assign_special_duty(area_name)

        # Redirect to the special duty page with the assigned members
        assigned_members = SpecialDuty.objects.filter(area_name=area_name)
        return render(request, 'basicuser/special_duty.html', {'assigned_members': assigned_members, 'area_name': area_name})

    # If the request method is not POST or the form is invalid, render the teamleader_special_duty page
    counters = Counter.objects.all()
    available_sections = section.objects.all()
    available_zone = zone.objects.all()
    available_room = room_number.objects.all()
    available_counter = Counter.objects.all()

    # Add the form to the context
    context = {
        'counters': counters,
        'available_sections': available_sections,
        'available_zone': available_zone,
        'available_room': available_room,
        'available_counter': available_counter,
        'form': form,
    }

    return render(request, 'basicuser/teamleader_special_duty.html', context)


def unassign_clerk_special_duty3(request):
    form = SpecialDutyAssignmentForm2(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Handle form submission to unassign and assign special duty
        selected_clerk = form.cleaned_data['clerk']
        area_name = form.cleaned_data['area_name']

        # Create SpecialDuty instances for selected clerks
        for clerk in selected_clerk:
            clerk.assign_special_duty(area_name)

        # Redirect to the special duty page with the assigned members
        assigned_members = SpecialDuty.objects.filter(area_name=area_name)
        return render(request, 'basicuser/special_duty.html', {'assigned_members': assigned_members, 'area_name': area_name})

    # If the request method is not POST or the form is invalid, render the clerk_special_duty page
    counters = Counter.objects.all()
    available_sections = section.objects.all()
    available_zone = zone.objects.all()
    available_room = room_number.objects.all()
    available_counter = Counter.objects.all()

    # Add the form to the context
    context = {
        'counters': counters,
        'available_sections': available_sections,
        'available_zone': available_zone,
        'available_room': available_room,
        'available_counter': available_counter,
        'form': form,
    }

    return render(request, 'basicuser/clerk_special_duty.html', context)





# views.py
# views.py
from django.shortcuts import render


def special_duty_view3(request):
    all_duty_members = SpecialDuty.objects.all()
    return render(request, 'basicuser/special_duty.html', {'all_duty_members': all_duty_members})



