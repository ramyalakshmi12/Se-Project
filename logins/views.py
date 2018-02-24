from django.shortcuts import render, HttpResponse, redirect, reverse
import pyrebase

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

def base(request):
	return render(request, 'base.html')

def signin(request, error = ''):
	return render(request,'signin/signin.html', {"error": error})

def signup(request):
	return render(request, 'signup/signup.html')

def postsignin(request):
	email = request.POST.get('email')
	passw = request.POST.get('password')
	try:
	    user = auth.sign_in_with_email_and_password(email,passw)
	except:
	    message="invalid info"
	    return redirect(reverse(signin))
	return render(request,'profile/profile.html')

def postsignup(request):
    name  = request.POST.get("name")
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = auth.create_user_with_email_and_password(email,passw)
    except:
            message="invalid info"
            return render(request,'signup/signup.html',{"messg":message})
    return render(request,'base.html',{"e":email})

def logout(request):
	auth.logout(request)
	return render(request, 'base.html')

def profile(request):
    email = request.POST.get("email")
    print("\n\n\nENTER\n\n\n")
    try:
        print("\n\n\nchecking\n\n\n")
        user = auth.send_password_reset_email(email)
    except:
        message="invalid info"
        print("\n\n\nNOT WORKING\n\n\n")
        return render(request, 'base.html', {"messg":messsage})
    print("\n\n\nWORKING\n\n\n")
    return render(request, 'profile/profile.html')