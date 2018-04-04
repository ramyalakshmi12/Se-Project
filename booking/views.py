from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth as authe
from logins import views as v
user = {}

# Create your views here.
config = {
    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com/",
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
        print()
        #request.session['b_no']+=1
        #db.child("users").child(request.session['key']).child("journey").push(data)
        request.session['store']=data
        j=0
        d={}
        for i in db.child('avialable').get().each():
            print('haha  ',i.val(),j,i.key())
            if i.val()!=None:
                d[j]=i.val()
            j+=1
        return render(request, 'flight_bookings/show.html',{'all': d})
    else:
        return redirect(reverse(v.signin))




def seat(request):
    for i in range(1,10):
        if str(i) in request.POST:
            request.session['rtno']=str(i)
    return render(request,'seat.html')



def details(request):
    print(request.session['key'])
    x = db.child('users').child(request.session['key']).child('journey').get()
    w ={}
    for i in x.each():
        w[i.key()]=(i.val())
    print('x value \n\n\n\n\n\n')
    print('hello \n',w)
    return render(request,'details.html', {'all':w})
    print('\n\n\n\n\n\n')
    print(x.val())
    #return HttpResponse(x.val())
    #return render(request,'details.html',{'all': x })




def done(request):
    seats=[]
    cnt=0
    y=0
    for i in range(1,13):
        y = request.POST.get(str(i))
        if y=='on':
            print(y)
            cnt+=1
            seats.append(i)
    print(request.session['key'])
    data = request.session['store']
    data['seats']=seats
    db.child('users').child(request.session['key']).child('journey').child(request.session['rtno']).set(data)

    return redirect(details)
