from django.shortcuts import render, redirect
from .models import User
from .forms import InterestForm, SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages


currentname = ""    # current user name
currentinterest = "snapping" # current user interest

def main(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def suggestion(request):
    #if name == "":
        #return render(request, 'base.html')
    #else:
    currentinterestlst = currentinterest.split(",")
    recomendedpeople = []
    users =  User.objects.all().values() # TODO Implement this
    for data in users:
        interest = data.get('interest')
        interestlst = interest.split(",")
        if set(interestlst).intersection(currentinterestlst) != set():
            recomendedpeople.append({'fullname':data.get('fullname'), 'interest':interest})

    #set notes as a collection of object Notes
    response = {'users': recomendedpeople}
    return render(request, 'suggestion.html', response) #temporary html page

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
    global currentname
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
    global currentname
    #form = LoginForm(request.POST or None)

    if request.method == 'POST':
        print(User.objects.get(username='galahad'))
        #if form.is_valid():
            
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
                currentname = username
                #currentname = form.cleaned_data.get('username')
                print(currentname)

                return redirect('/')
           
            #messages.error(request, "Unsuccessful registration. Invalid information.")
    
    forms = {}
    
    
    return render(request, "login.html", forms)

    



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
