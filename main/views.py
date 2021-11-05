from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import User, ThreadModel, MessageModel
from .forms import InterestForm, SignupForm, LoginForm, ThreadForm, EditForm
from django.contrib.auth import login
from django.contrib import messages
from django.http.response import HttpResponse
from django.core import serializers
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
            interestlst = interest.split(",")[0:-1]
            intersection = set(interestlst).intersection(currentinterestlst)

            if intersection != set() and data.get('fullname') != currentname:
                intersection = list(intersection)
                if len(intersection) > 5:
                    intersection = intersection[0:5]
                    intersection.append(" and more...")
                interest = "Both of you like " + ','.join(intersection)
                recomendedpeople.append({'fullname':data.get('fullname'), 'DOB':data.get('DOB'),'email':data.get('email'),'instagram':data.get('instagram'),'line':data.get('line'),'interest':interest,'domicile':data.get('domicile'),'gender':data.get('gender')})

        #set notes as a collection of object Notes
        response = {'users': recomendedpeople, 'currentname': currentname, 'username':currentusername}
        return render(request, 'suggestion.html', response) #temporary html page

    except:
        return redirect('/login')


def profile(request):
    context = {}
    instance = User.objects.get(username=currentusername)
    form = InterestForm(request.POST or None, instance = instance)

    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            notes = User.objects.all()
            response = {'notes': notes}
            return redirect('/suggestion')

    context = {'form':form, 'username':currentusername, 'email':currentemail}
    return render(request, "profile_form.html", context)

def signup_request(request):
    global currentusername, currentemail
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        #print(form.is_valid())
        if form.is_valid():

            form.save()
            #login(request, user)

            currentusername = form.cleaned_data.get('username')
            currentemail = form.cleaned_data.get('email')

            return redirect('/profile')
        #messages.error(request, "Unsuccessful registration. Invalid information.")

    forms = {'user': form}

    return render(request, "signup.html", forms)

def login_request(request):
    global currentusername, currentname, currentDOB, currentemail, currentig, currentline, currentinterest, currentdomicile, currentgender, currentpassword
    # form = LoginForm(request.POST or None)
    currentname = None
    currentDOB = None
    currentemail = None
    currentig = None
    currentline = None
    currentinterest = None
    currentdomicile = None
    currentgender = None
    currentpassword = None
    if request.method == 'POST':
        username = request.POST.get('Username')
        print(username, 'welcome!')
        try:
            user = User.objects.get(username=username)
            print(user)
        except:
            redirect('/login')
            print('welcome!')
        else:
            password_input = request.POST.get('password')
            password = user.password

            # print(form.is_valid())
            # login(request, user)
            if password == password_input:
                messages.success(request, 'sucessful!')
                currentusername = user.username
                currentname = user.fullname
                currentDOB = user.DOB
                currentemail = user.email
                currentig = user.instagram
                currentline = user.line
                currentinterest = user.interest
                currentdomicile = user.domicile
                currentgender = user.gender
                currentpassword = user.password

                # if the user haven't filled out the form
                if currentname == '' or currentig == '' or currentline == '' or currentinterest == '' or currentdomicile == '' or currentgender == '':
                    return redirect("/profile")
                # currentname = form.cleaned_data.get('username')

                return redirect("/suggestion")

            # messages.error(request, "Unsuccessful registration. Invalid information.")

    forms = {}

    return render(request, "login.html", forms)


def randomize(request):
    users = list(User.objects.all())
    users = random.sample(users,1)
    random_users = random.choice(users)
    return render(request, 'random.html', {'users': random_users})


def getList(request):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

    context = {
        'threads' : threads
    }

    return render(request, 'inbox.html', context)

class CreateThread(View):
    def get(request):
        form = ThreadForm()
        context = {
            'form' : form
        }
        return render(request, 'create_thread.html', context)

    def post(request):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user = request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user = request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user = receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(user = request.user, receiver = receiver)
                thread.save()

                return redirect('thread', pk = thread.pk)
        except:
            return redirect('create-thread')

def profile_edit(request):
    global currentusername, currentname, currentDOB, currentemail, currentig, currentline, currentinterest, currentdomicile, currentgender, currentpassword
    context = {}
    formerusername = currentusername
    user = User.objects.get(username=currentusername)
    form = EditForm(request.POST or None, instance=user)

    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            currentusername = user.username
            currentname = user.fullname
            currentemail = user.email
            currentig = user.instagram
            currentline = user.line
            currentinterest = user.interest
            currentdomicile = user.domicile
            currentpassword = user.password
            if formerusername != currentusername:
                User.objects.get(username=formerusername).delete()
            return redirect("/suggestion")

    context = {'form': form, 'username': currentusername, 'name': currentname, 'DOB': currentDOB,
               'email': currentemail,
               'instagram': currentig, 'line': currentline, 'interest': currentinterest,
               'domicile': currentdomicile,
               'password': currentpassword, 'gender': currentgender}
    return render(request, "profile_edit.html", context)

def json(request):
    data = serializers.serialize('json', User.objects.all())
    return HttpResponse(data, content_type="application/json")

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
