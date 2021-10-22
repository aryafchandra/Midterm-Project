from django.shortcuts import render
from .models import User
from .forms import InterestForm

def main(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

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
