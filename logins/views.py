from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth as authe
from booking import views as v
user = {}
x = 0
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

def base(request):
    '''if 'uid' in request.session:
        keep = auth.get_account_info(request.session['uid'])
        if keep['users'][0]['emailVerified']:
            return 0;
        email = keep['users'][0]['email']'''
    mesg = ''
    if 'emailVerificationMesg' in request.session:
        mesg = request.session.get('emailVerificationMesg')
        request.session.pop('emailVerificationMesg', None)

    return render(request, 'base.html', {'mesg': mesg})

def signin(request):
    error = ''
    if 'mesg' in request.session:
        error = request.session.get('mesg')
        request.session.pop('mesg', None)
    return render(request,'signin/signin.html', {'error': error})

def signup(request):
    return render(request, 'signup/signup.html', {})

def postsignin(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email,passw)

    except:
        message="invalid info"
        request.session['mesg'] = 'Invalid Username or Password'
        request.session['mesgcount'] = int(2)
        x = 0
        return redirect(reverse(signin))
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    x = 1
    print("in login. views x = ",x)
    return redirect(v.book)

def postsignup(request):
    name  = request.POST.get("uname")
    email = request.POST.get("cemail")
    passw = request.POST.get("password")
    gender = request.POST.get("cgender")
    agree = request.POST.get("cagree")
    print("name = " + str(name) )
    print("email = " + str(email) )
    print("passw = " + str(passw) )
    print("gender = " + str(gender) )
    print("agree = " + str(agree) )
    try:
        user = auth.create_user_with_email_and_password(email, passw)
        auth.send_email_verification(user['idToken'])
        data = { 'name': name,
                 'email': email,
                 'gender': gender
               }
        db.child("users").child(email.split('@')[0]).set(data)
        x = 1
        request.session['emailVerificationMesg'] = 'Verification email has been sent'
    except:
            message="invalid info"
            x = 0
            return render(request,'signup/signup.html',{"messg":message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return redirect(v.book)

def logout(request):
    auth.logout(request)
    x = 0
    return render(request, 'base.html')

def profile(request):
    return render(request, 'profile/profile.html')

def resetpassword(request):
    email = request.POST.get("email")
    try:
        user = auth.send_password_reset_email(email)
    except:
        message="invalid info"
        return render(request, 'base.html', {"messg":message})
    return redirect(reverse(profile))
