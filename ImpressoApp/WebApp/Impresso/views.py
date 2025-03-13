from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .models import Prize
# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email is already in use'})
        
        # Create a new user object
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        # Redirect to the login page
        return redirect('login')
    
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

@require_http_methods(["GET"])
def location(request):
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return JsonResponse({'error': 'Forbidden'}, status=403)
    return render(request, 'location.html')

@require_http_methods(["GET"])
def contact(request):
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return JsonResponse({'error': 'Forbidden'}, status=403)
    return render(request, 'contact.html')

@require_http_methods(["GET"])
def about(request):
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return JsonResponse({'error': 'Forbidden'}, status=403)
    return render(request, 'about.html')

@require_http_methods(["GET"])
def menu(request):
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return JsonResponse({'error': 'Forbidden'}, status=403)
    return render(request, 'menu.html')

@csrf_exempt
def reservation(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        guests = request.POST['people']
        if Reservation.objects.filter(date=date, time=time).exists():
            return render(request, 'reservation.html', {'failed': 'Reservation at this hour already exists'})
        # Save the reservation to the database
        reservation = Reservation(name=name, phone=phone, email=email, date=date, time=time, nr_of_people=guests)
        reservation.save()
        return render(request, 'home.html', {'success': 'Reservation made successfully'})
    
    return render(request, 'reservation.html')

def staff_rezervari(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    reservations = Reservation.objects.all()
    return render(request, 'staff_rezervari.html', {'reservations': reservations})

def staff_clienti(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    users = User.objects.all()
    prize = Prize.objects.all()
    return render(request, 'staff_clienti.html', {'users': users, 'prizes': prize})

def staff_RoataNorocului(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        check = request.POST['check']
        prize = request.POST['prize']
        print(f'Prize: {prize}, Phone: {phone}, Name: {name}', check)
        # Save the prize to the database
        prize_entry = Prize(name=name, phone=phone, bon=check, prize=prize)
        prize_entry.save()
    
    return render(request, 'staff_RoataNorocului.html', {'success': 'Prize recorded successfully'})

@csrf_exempt
def delete_reservation(request, id):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'DELETE':
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
        print('Deleted reservation')
        return redirect('staff_rezervari')
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)