from django.contrib import admin
from django.urls import path
from projectApp import views

urlpatterns = [
   path("",views.index, name='projectApp'),
   path("index/",views.index, name='projectApp'),
   path('contact/', views.contact, name='contact'),
   #path("result", views.result, name='result'),
   #path("input", views.input, name='input'),
   #path("fakenew", views.fakenew, name='fakenew'),
   #path("result_new", views.result_new, name='result_new'),
   # path("login1",views.login1, name='login1'),
   # path("logout_request/",views.logout_request,name='logout_request'),
   path("feature/", views.feature, name="feature"),
  # path("register/", views.register, name="register"),
   path("about/", views.about, name="about"),
   path("service/", views.service, name="service"),
   #path("input1", views.input1, name='input1'),
   # path('home/', views.home, name='home'),
   path('book_appointment/', views.book_appointment, name='book_appointment'),
   path("testiminial/", views.testiminial, name="testiminial"),
   path("chatbot_response/", views.chatbot_response, name="chatbot_response"),
   path("chatbot/", views.open_chat_window, name="chatbot"),
 

  
]