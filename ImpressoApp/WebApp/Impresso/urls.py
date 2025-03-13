from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),  
    path('register', views.register, name='signup'),  
    path('logout', views.logout_view, name='logout'),
    path('location', views.location, name='location'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('reservation', views.reservation, name='reservation'),
    path('staff/rezervari', views.staff_rezervari, name='staff_rezervari'),
    path('staff/clienti', views.staff_clienti, name='staff_clienti'),
    path('staff/RoataNorocului', views.staff_RoataNorocului, name='staff_RoataNorocului'),
    path('reservations/delete/<int:id>', views.delete_reservation, name='delete_reservation'),
]


