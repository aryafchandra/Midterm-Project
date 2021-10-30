from django.shortcuts import render, redirect
from .models import User
from .forms import InterestForm, SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages
import random

def main(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def suggestion(request):
    try:
        currentinterestlst = currentinterest.split(",")
        recomendedpeople = []
        users =  User.objects.all().values() # TODO Implement this
        for data in users:
            interest = data.get('interest')
            interestlst = interest.split(",")
            if set(interestlst).intersection(currentinterestlst) != set():
                recomendedpeople.append({'fullname':data.get('fullname'), 'DOB':data.get('DOB'),'email':data.get('email'),'instagram':data.get('instagram'),'line':data.get('line'),'interest':interest,'domicile':data.get('domicile'),'gender':data.get('gender')})

        #set notes as a collection of object Notes
        response = {'users': recomendedpeople}
        return render(request, 'suggestion.html', response) #temporary html page

    except:
        return redirect('/login')


def profile(request):
    context = {}

    form = InterestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            notes = User.objects.all()
            response = {'notes': notes}
            return render(request, 'homepage.html', response)

    context['form'] = form
    return render(request, "profile_form.html", context)

def signup_request(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        #print(form.is_valid())
        if form.is_valid():

            form.save()
            #login(request, user)

            currentname = form.cleaned_data.get('username')

            return redirect('/profile')
        #messages.error(request, "Unsuccessful registration. Invalid information.")

    forms = {'user': form}

    return render(request, "signup.html", forms)

def login_request(request):
    global currentname, currentDOB, currentemail, currentig, currentline, currentinterest, currentdomicile, currentgender
    #form = LoginForm(request.POST or None)

    if request.method == 'POST':


        username = request.POST.get('Username')
        print(username,'hai')
        try:
            user = User.objects.get(username=username)
            print(user)
        except:
            redirect('/login')
            print('hai')
        else:
            password_input = request.POST.get('password')
            password = user.password


            #print(form.is_valid())
                #login(request, user)
            if password == password_input:
                messages.success(request, 'anjas bisa')
                currentname = user.fullname
                currentDOB = user.DOB
                currentemail = user.email
                currentig = user.instagram
                currentline = user.line
                currentinterest = user.interest
                currentdomicile = user.domicile
                currentgender = user.gender
                #currentname = form.cleaned_data.get('username')
                print(currentname,currentDOB,currentinterest,currentemail,currentgender)

                return redirect("/suggestion")

            #messages.error(request, "Unsuccessful registration. Invalid information.")

    forms = {}


    return render(request, "login.html", forms)

def randomize(request):
    users = list(User.objects.all())
    users = random.sample(users,1)
    random_users = random.choice(users)
    return render(request, 'random.html', {'users': random_users})

#def getProfile(request):




# def checklist(request):

#     checkbox = InterestForm(request.POST or None)

#     if checkbox.method=="POST":
#         if (request.POST.get('checkvalue')):
#             savedata = User.interest()
#             savedata.interest = request.POST.get('interest')
#             savedata.save()
#             return render(request, 'checklist.html')
#         else:
#             return render(request, 'checklist.html')
