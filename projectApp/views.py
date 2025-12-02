from django.db import IntegrityError
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from .forms import ContactForm
import os
import time
import random
import requests
import requests
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
import numpy as np
import joblib
from django.contrib.auth.models import User
import os
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from .forms import ContactForm
from .models import ContactMessage
# Create your views here.
def index(request):
        return render(request, 'index.html')
        



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact')
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

        

#############3--------------------------------------GUI Part-------------------------------------------
def feature(request):
    return render(request, 'feature.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

from .forms import AppointmentForm

from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Doctor

def testiminial(request):
    return render(request, 'testiminial.html')

def open_chat_window(request):
    return render(request, "chatbot.html")

from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure API key (replace with your actual key)
genai.configure(api_key="AIzaSyApNvCXc7N9Vv-m_MC-UIygtvpG1-6WWg0")

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

def book_appointment(request):
    return render(request, "appointment.html")  # Frontend page

def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        print("Received:", user_message)  # Debug
        if not user_message:
            return JsonResponse({"error": "No message provided."})

        # Call Gemini model
        response = model.generate_content(user_message)

        return JsonResponse({"response": response.text})

    return JsonResponse({"error": "Invalid request."})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login1')