from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
import json
from django.core.paginator import Paginator
import pdfkit
from django.template.loader import get_template
from xhtml2pdf import pisa

from app.forms import *
from app.models import *





def home4(request):
    if request.method == "POST":
        contact = contact_us(
            
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
        
    return render(request,'users/home4.html')



def vehicle_alloted(request):
    return render(request,'users/vehicle_alloted_details.html')




def download_id_card_download(request):
    # users = Users.objects.all()
    
    template_path = 'users/download_id_card_download.html'
    # context = {'users': users}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render() # print (context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def message_from_admin(request):
    messages = user_message.objects.all().order_by('-timestamp')
    return render(request, 'users/message_from_admin4.html', {'messages': messages})


def message_from_superuser(request):
    messages = superuser_user.objects.all().order_by('-timestamp')
    return render(request, 'users/message_from_superuser4.html', {'messages': messages})


def message_from_basicuser(request):
    messages = basicuser_user.objects.all().order_by('-timestamp')
    return render(request, 'users/message_from_basicuser4.html', {'messages': messages})




def message_sent_user(request):
    return render (request,'users/message_sent_user.html')



def send_message_basicuser(request):
    if request.method == 'POST':
        form = user_to_basicuser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent_user')
    else:
        form = user_to_basicuser()
    return render(request, 'users/basicuser_broadcast4.html', {'form': form})




def send_message_superuser(request):
    if request.method == 'POST':
        form = user_to_superuser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent_user')
    else:
        form = user_to_superuser()
    return render(request, 'users/superuser_broadcast4.html', {'form': form})




def admit_card_access(request):
    error_message = None

    if request.method == 'POST':
        contact = request.POST.get('contact')
        emp_code = request.POST.get('emp_code')

        try:
            # Assuming contact is a field in the Member model
            member = Member.objects.get(contact=contact, emp_Code=emp_code)
            
            # Redirect to the admit card page with the member's ID
            return redirect('user_home4')
        except Member.DoesNotExist:
            # Check if neither contact nor emp_code exists in the database
            if not Member.objects.filter(contact=contact).exists() and not Member.objects.filter(emp_Code=emp_code).exists():
                error_message = "You are not a user. Please check your details and try again."
            else:
                error_message = "Member not found with the provided contact and emp code."

    return render(request, 'admit_card_access.html', {'error_message': error_message})


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

    return render(request, 'users/admit_card.html', context)


def admit_card_search(request):
    error_message = None

    if request.method == 'POST':
        contact = request.POST.get('contact')
        

        try:
            # Assuming contact is a field in the Member model
            member = Member.objects.get(contact=contact)
            
            # Redirect to the admit card page with the member's ID
            return redirect('admit_card', member_id=member.id)
        except Member.DoesNotExist:
            # Check if neither contact nor emp_code exists in the database
            if not Member.objects.filter(contact=contact).exists():
                error_message = "You are not a user. Please check your details and try again."
            else:
                error_message = "Member not found with the provided contact and emp code."
        
        # Add this line for debugging
        print(f"Error Message: {error_message}")

    return render(request, 'users/admit_card_search.html', {'error_message': error_message})
