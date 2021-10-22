from django.shortcuts import render
from .models import User

currentname = ""
currentinterest = "snapping"

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
    print(users)
    for data in users:
        interest = data.get('interest')
        interestlst = interest.split(",")
        print(set(interestlst).intersection(currentinterestlst))
        if set(interestlst).intersection(currentinterestlst) != set():
            recomendedpeople.append({'name':data.get('name'), 'interest':interest})

    #set notes as a collection of object Notes
    response = {'users': recomendedpeople}
    print(response)
    return render(request, 'suggestion.html', response)
