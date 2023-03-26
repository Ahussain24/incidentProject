from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import Incident
from .forms import IncidentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from django.urls import reverse
from django.utils.html import strip_tags
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import IncidentSerializer
from django.conf import settings

@login_required
def index(request):
    # get the user information from the request object
    user = request.user
    
    # get all incidents created by the user
    incidents = Incident.objects.filter(reporter=user)
     # print all incidents line by line
    # for incident in incidents:
    #     print(f"Incident ID: {incident.incident_id}")
    #     print(f"Reporter Name: {incident.reporter}")
    #     print(f"Incident Details: {incident.incident_details}")
    #     print(f"Reported Date/Time: {incident.reported_date}")
    #     print(f"Priority: {incident.priority}")
    #     print(f"Incident Status: {incident.status}")
    
    # render the index.html template with user information and incidents
    return render(request, 'index.html', {'user': user, 'incidents': incidents})

@login_required
def create_incident(request):
    if request.method == 'POST':
        # Handle the form submission
        reporter = request.user
        incident_details = request.POST['incident_details']
        reported_date = request.POST['reported_date']
        priority = request.POST['priority']
        status = request.POST['incident_status']
        print(reporter, incident_details, reported_date, priority, status)
        
        # Create a new incident object
        incident = Incident(
            reporter=reporter,
            incident_details=incident_details,
            reported_date=reported_date,
            priority=priority,
            status=status,
        )
        incident.save()
        
        # Redirect to the same page with a success message
        messages.success(request, 'Incident reported successfully!')
        return redirect('create_incident')
        
    else:
        # Render the form template
        context = {
            'user': request.user,
        }
        return render(request, 'create_incident.html', context)




def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Replace 'index' with the name of your home page URL pattern
        else:
            # Invalid login credentials
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
            except IntegrityError:
                error_message = 'Username already taken. Please choose a different username.'
                return render(request, 'register.html', {'form': form, 'error_message': error_message})
            success_message = 'Registration successful! Please log in.'
            login_url = reverse('login') + f'?success_message={success_message}'
            return redirect(login_url)
        else: 
            error_list = []
            error_message = ''
            for field, errors in form.errors.items():
                text = f'{field}: {strip_tags(errors)}'.split(':')[-1]
                error_list.append(text)

            error_message += '\n'.join(error_list)
            return render(request, 'register.html', {'form': form, 'error_message': error_message})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def update_incident(request):
    if request.method == 'GET':
        # Retrieve the incident from the database and prefill the form fields
        incident_id = request.GET.get('incident_id')

        print("Need to update ", incident_id)
        incident = get_object_or_404(Incident, incident_id=incident_id)
        print(incident.status)
        print(Incident.INCIDENT_STATUS_OPEN, Incident.INCIDENT_STATUS_IN_PROGRESS)
        if incident.status in [Incident.INCIDENT_STATUS_OPEN, Incident.INCIDENT_STATUS_IN_PROGRESS]:
            user = request.user
            return render(request, 'update_incident.html', {"user": user, "incident": incident})
        else:
            message = "Incident not found or cannot be updated"
            messages.error(request, message)
            return redirect('index')
    else:
        # Handle the form submission
        incident_id = request.POST['incident_id']
        incident = get_object_or_404(Incident, incident_id=incident_id)
        if incident.status in [Incident.INCIDENT_STATUS_OPEN, Incident.INCIDENT_STATUS_IN_PROGRESS]:
            incident.incident_details = request.POST['incident_details']
            incident.priority = request.POST['priority']
            incident.status = request.POST['incident_status']
            incident.save()
            messages.success(request, 'Incident updated successfully!')
            print(incident)
        else:
            messages.error(request, 'Incident cannot be updated')
        return redirect('index')


@login_required 
def incidents(request): 
    user = request.user
    return render(request, 'incidents.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_incidents(request):
    user = request.user
    incidents = Incident.objects.filter(reporter=user)
    serializer = IncidentSerializer(incidents, many=True)
    return Response({'user': user.username, 'incidents': serializer.data})
    







