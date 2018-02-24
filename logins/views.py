from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase
from django.contrib import auth

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
authe = firebase.auth()

def base(request):
    keep = authe.get_account_info(user['idToken'])

    '''if not(keep['users'][0]['emailVerified']):
        return 0;'''
    email = keep['users'][0]['email']
    return render(request, 'base.html')

def signin(request, error = ''):
	return render(request,'signin/signin.html', {"error": error})

def signup(request):
	return render(request, 'signup/signup.html')

def postsignin(request):
    global user
    email = request.POST.get('email')
    passw = request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid info"
        return redirect(reverse(signin))
    print(user['localId'])
    session_id = user['localId']
    request.session['uid'] = str(session_id)

    return redirect(reverse(base))

def postsignup(request):
    name  = request.POST.get("name")
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = authe.create_user_with_email_and_password(email,passw)
    except:
            message="invalid info"
            return render(request,'signup/signup.html',{"messg":message})

    return render(request,'base.html',{"e":email})

def logout(request):
	authe.logout(request)
	return render(request, 'base.html')

def profile(request):
    return render(request, 'profile/profile.html')

def resetpassword(request):
    email = request.POST.get("email")
    try:
        user = authe.send_password_reset_email(email)
    except:
        message="invalid info"
        return render(request, 'base.html', {"messg":messsage})
    return redirect(reverse(profile))
