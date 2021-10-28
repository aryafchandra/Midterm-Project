from django.shortcuts import render
from .models import User
from .forms import ProfileForm

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

    form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # save the form data to model
            form.save()
            notes = User.objects.all()
            response = {'notes': notes}
            return render(request, 'homepage.html', response)

    context['form'] = form
    return render(request, "profile_form.html", context)

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
