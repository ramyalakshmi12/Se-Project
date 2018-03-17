from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth as authe
from logins.views import x
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
    print("in booking. views x = ",x)
    return render(request,'flight_bookings/book.html')
def postbooking(request):
    print("in booking. views x = ",x)
    begin = request.POST.get("from")
    to = request.POST.get("to")
    date = request.POST.get("Date")
    data = { 'from' :begin,
              'to' :to,
              'date': date
            }
    if x ==1 :
        db.child("users").child("journey").set(data)
        return render(request,'logins/signin/sign.html')
    else:
        return HttpResponse('wrong!!')
