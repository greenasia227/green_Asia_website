from django.contrib import admin
from django.urls import path
from projectApp import views

urlpatterns = [
   path("",views.index, name='projectApp'),
   path("index/",views.index, name='projectApp'),
   path('contact/', views.contact, name='contact'),
   path("feature/", views.feature, name="feature"),
   path("about/", views.about, name="about"),
   path("service/", views.service, name="service"),
   path('book_appointment/', views.book_appointment, name='book_appointment'),
   path("testiminial/", views.testiminial, name="testiminial"),
   path("chatbot_response/", views.chatbot_response, name="chatbot_response"),
   path("chatbot/", views.open_chat_window, name="chatbot"),
 

  
]