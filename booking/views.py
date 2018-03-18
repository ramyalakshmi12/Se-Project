from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth as authe
from logins import views as v
user = {}

# Create your views here.
config = {
    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com",
    'projectId': "software-engineering-6e9a7",
    'storageBucket': "software-engineering-6e9a7.appspot.com",
    'messagingSenderId': "329135496498"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
def book(request):
    return render(request,'flight_bookings/book.html')
def postbooking(request):
    begin = request.POST.get("from")
    to = request.POST.get("to")
    date = request.POST.get("Date")
    passengers = request.POST.get("pass")
    data = { 'from' :begin,
              'to' :to,
              'date': date,
              'passengers': passengers
            }
    if 'uid' in request.session :
        print("\n\n\n\n")
        print(passengers)
        db.child("users").child(request.session['key']).child("journey").set(data)
        return HttpResponse("DONE")
    else:
        return redirect(reverse(v.signin))
