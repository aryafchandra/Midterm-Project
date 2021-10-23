from django.shortcuts import render
from .models import User
from .forms import InterestForm

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

def interest(request):
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
    return render(request, "forms.html", context)
