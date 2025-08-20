from django.urls import path 

from . import views

app_name = 'hello'

urlpatterns = [
    # Home page

    path("", views.home, name= 'home'),

    # received page

    path('received', views.received, name ='received'),

     # remaining page

    path('remaining', views.remaining, name ='remaining'),

     # sold page

    path('sold', views.sold, name ='sold')
]